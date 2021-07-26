from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Video
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

SCROLL_LIMIT = 3
CATEGORY_LIMIT = 0
SUB_CATEGORY_LIMIT = 1


def save_videos(driver, videos, sub_category_name, category_name):
    for video in videos:
        driver.get(video['url'])
        try:
            download_link = driver.find_element_by_xpath("//div[@class='dropdown-content']/div[@class='menu-wrapper']/ul[@class='menu-list']/li[@class='menu-item-link link']/a").get_attribute('href')
        except NoSuchElementException:
            download_link = ""
        new_video = Video(title=video['name'], category_name = category_name, sub_category_name = sub_category_name, url = video['url'], download_link=download_link)
        new_video.save()


def crawl_video(driver, sub_category, category_name):
    driver.get(sub_category['url'])

    for i in range(SCROLL_LIMIT):
        html_element= driver.find_element_by_tag_name('html')
        html_element.send_keys(Keys.END)
        time.sleep(1)

    videos_object = driver.find_elements_by_xpath( "//div[@class='thumb-details']/div[@class='thumb-title']/a")

    videos = []

    for video in videos_object:
        videos.append({'name': video.text, 'url':video.get_attribute('href')})

    save_videos(driver, videos, sub_category['name'], category_name)


def crawl_category(driver, category):
    driver.get(category['url'])

    for i in range(SCROLL_LIMIT):
        html_element= driver.find_element_by_tag_name('html')
        html_element.send_keys(Keys.END)
        time.sleep(1)

    sub_categories_object = driver.find_elements_by_xpath( "//div[@class='item']/div[@class='inline-flex list-header-title']/h3[@class='list-title']/a")

    sub_categories = []

    for sub_category in sub_categories_object:
        sub_categories.append({'name': sub_category.get_attribute('title'), 'url':sub_category.get_attribute('href')})

    for i in range(SUB_CATEGORY_LIMIT):
        crawl_video(driver, sub_categories[i], category['name'])



def crawl_aparat(request):
    driver = webdriver.Firefox()
    driver.get("https://www.aparat.com/")

    more_button = driver.find_element_by_xpath("//ul[@class='menu-list']/li[@class='menu-item-link menu-show-more']/a")
    more_button.click()

    categories_object = driver.find_elements_by_xpath( "//div[@id=2]/ul[@class='menu-list']/li[@class='menu-item-link']/a")

    categories = []

    for category in categories_object:
        categories.append({'name': category.text, 'url':category.get_attribute('href')})
    

    for i in range(CATEGORY_LIMIT):
        crawl_category(driver, categories[i])

