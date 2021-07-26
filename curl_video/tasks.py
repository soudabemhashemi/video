from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@shared_task
def crawl_aparat():
    pass
    # driver = webdriver.Firefox()
    # driver.get("https://www.aparat.com/")

    # more_button = driver.find_element_by_xpath("//ul[@class='menu-list']/li[@class='menu-item-link menu-show-more']/a")
    # more_button.click()

    # select = driver.find_element_by_xpath( "//div[@id=2]")
    # categories_object = select.find_elements_by_xpath( "//div[@id=2]/ul[@class='menu-list']/li[@class='menu-item-link']/a")

    # categories = []

    # for category in categories_object:
    #     categories.append({'name': category.text, 'url':category.get_attribute('href')})
    

    # print(categories)



