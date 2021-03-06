from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from .models import Video, CategoryCatalog

SCROLL_LIMIT = 3
SUB_CATEGORY_LIMIT = 1

@shared_task
def crawl_category(category):
    driver = webdriver.Firefox()
    driver.get(category['url'])

    for i in range(SCROLL_LIMIT):
        html_element= driver.find_element_by_tag_name('html')
        html_element.send_keys(Keys.END)
        time.sleep(1)

    sub_categories_object = driver.find_elements_by_xpath( "//div[@class='item']/div[@class='inline-flex list-header-title']/h3[@class='list-title']/a")

    sub_categories = []

    for sub_category in sub_categories_object:
        sub_categories.append({'name': sub_category.get_attribute('title'), 'url':sub_category.get_attribute('href')})

    local_limit = SUB_CATEGORY_LIMIT
    if len(sub_categories) < SUB_CATEGORY_LIMIT:
        local_limit = len(sub_categories)

    for i in range(0, local_limit):
        crawl_video.delay(sub_categories[i], category['name'])
    driver.close()


@shared_task
def crawl_video(sub_category, category_name):
    driver = webdriver.Firefox()
    driver.get(sub_category['url'])

    for i in range(SCROLL_LIMIT):
        html_element= driver.find_element_by_tag_name('html')
        html_element.send_keys(Keys.END)
        time.sleep(1)

    videos_object = driver.find_elements_by_xpath( "//div[@class='thumb-details']/div[@class='thumb-title']/a")

    videos = []

    for video in videos_object:
        videos.append({'name': video.text, 'url':video.get_attribute('href')})

    save_videos.delay(videos, sub_category['name'], category_name)
    driver.close()


@shared_task
def save_videos(videos, sub_category_name, category_name):
    driver = webdriver.Firefox()
    for video in videos:
        driver.get(video['url'])
        try:
            download_link = driver.find_element_by_xpath("//div[@class='dropdown-content']/div[@class='menu-wrapper']/ul[@class='menu-list']/li[@class='menu-item-link link']/a").get_attribute('href')
        except NoSuchElementException:
            download_link = ""
        
        tags = []
        tags_object = driver.find_elements_by_xpath("//div[@class='date-section fs-xxs light-60 dark-110']/div[@class='tag video-tag']/a")
        if tags_object:
            for tag in tags_object:
                tags.append(tag.get_attribute('title'))
        
        item_in_catalog = CategoryCatalog.objects.filter(category_name = category_name, sub_category_name = sub_category_name)
        if not item_in_catalog:
            item_in_catalog = CategoryCatalog(category_name = category_name, sub_category_name = sub_category_name)
            item_in_catalog.save()

        new_video = Video(title=video['name'], sub_category_id = item_in_catalog[0], url = video['url'], download_link=download_link, tag = tags)
        new_video.save()
    driver.close()

