from django.shortcuts import render
from django.views.generic.base import TemplateView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .tasks import crawl_category

SCROLL_LIMIT = 3
CATEGORY_LIMIT = 1


def crawl_aparat(request):
    driver = webdriver.Firefox()
    driver.get("https://www.aparat.com/")

    more_button = driver.find_element_by_xpath("//ul[@class='menu-list']/li[@class='menu-item-link menu-show-more']/a")
    more_button.click()

    categories_object = driver.find_elements_by_xpath( "//div[@id=2]/ul[@class='menu-list']/li[@class='menu-item-link']/a")

    categories = []

    for category in categories_object:
        categories.append({'name': category.text, 'url':category.get_attribute('href')})
    

    for i in range(0, CATEGORY_LIMIT):
        crawl_category.delay(categories[i])
    
    driver.close()

