from django.shortcuts import render
from django.views.generic.base import TemplateView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

def get_sub_categories(driver, link):
    driver.get(link)

    while(1):
        htmlelement= driver.find_element_by_tag_name('html')
        htmlelement.send_keys(Keys.END)
        time.sleep(1)
        try:
            l= driver.find_element_by_id("pageLoadMore")
        except NoSuchElementException:
            break

    select = driver.find_element_by_xpath( "//section[@class='lc-content clear']")
    options = select.find_elements_by_xpath( "//section[@class='list-item li']/div[@class='list-wrapper']/header[@class='list-header']/div[@class='item']/div[@class='inline-flex list-header-title']/h3[@class='list-title']/a")

    options_category_name = []
    options_category_url = []

    for option in options:
        options_category_name.append(option.text)
        options_category_url.append(option.get_attribute('href'))

    # for optionValue in options_category_name:
    #     print(optionValue)

    # print("______________________________________________________________________")

    for ins in options_category_url:
        get_sub_categories(driver, ins)


class getCategories(TemplateView):
    template_name = ""
    driver = webdriver.Firefox()
    driver.get("https://www.aparat.com/")

    elem = driver.find_element_by_xpath("//ul[@class='menu-list']/li[@class='menu-item-link menu-show-more']/a")
    elem.click()
    select = driver.find_element_by_xpath( "//div[@id=2]")
    options = select.find_elements_by_xpath( "//div[@id=2]/ul[@class='menu-list']/li[@class='menu-item-link']/a")

    options_category_name = []
    options_category_url = []

    for option in options:
        options_category_name.append(option.text)
        options_category_url.append(option.get_attribute('href'))

    # for optionValue in options_category_name:
    #     print(optionValue)

    for ins in options_category_url:
        get_sub_categories(driver, ins)

