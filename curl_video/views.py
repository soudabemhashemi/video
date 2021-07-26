from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Video
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

LIMIT = 3


def save_videos(videos, sub_category_name, category_name):
    for video in videos:
        new_video = Video(title=video['name'], category_name = category_name, sub_category_name = sub_category_name, url = video['url'])
        new_video.save()

def crawl_video(driver, sub_category, category_name):
    driver.get(sub_category['url'])

    for i in range(LIMIT):
        html_element= driver.find_element_by_tag_name('html')
        html_element.send_keys(Keys.END)
        time.sleep(1)


    videos_object = driver.find_elements_by_xpath( "//div[@class='grid-thumbnail']/div[@class='item grid-item']/div[@class='thumbnail-movie thumbnail-serial ']/div[@class='thumb-details']/div[@class='thumb-title']/a")

    videos = []

    for video in videos_object:
        videos.append({'name': video.text, 'url':video.get_attribute('href')})

    save_videos(videos, sub_category['name'], category_name)

def crawl_category(driver, category):
    driver.get(category['url'])

    for i in range(LIMIT):
        html_element= driver.find_element_by_tag_name('html')
        html_element.send_keys(Keys.END)
        time.sleep(1)


    sub_categories_object = driver.find_elements_by_xpath( "//section[@class='lc-content clear']/section[@class='list-item li']/div[@class='list-wrapper']/header[@class='list-header']/div[@class='item']/div[@class='inline-flex list-header-title']/h3[@class='list-title']/a")

    sub_categories = []

    for sub_category in sub_categories_object:
        sub_categories.append({'name': sub_category.text, 'url':sub_category.get_attribute('href')})

    crawl_video(driver, sub_categories[0], category['name'])



class getCategories():
    driver = webdriver.Firefox()
    driver.get("https://www.aparat.com/")

    more_button = driver.find_element_by_xpath("//ul[@class='menu-list']/li[@class='menu-item-link menu-show-more']/a")
    more_button.click()

    categories_object = driver.find_elements_by_xpath( "//div[@id=2]/ul[@class='menu-list']/li[@class='menu-item-link']/a")

    categories = []

    for category in categories_object:
        categories.append({'name': category.text, 'url':category.get_attribute('href')})
    

    crawl_category(driver, categories[0])
    

