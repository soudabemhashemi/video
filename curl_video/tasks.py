from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

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



# @shared_task
# def summary_in_last_day():
#     t = datetime.now()
#     last_day = t.replace(day=int(t.strftime("%d"))-1)
#     ad_list = Ad.objects.all()
#     for ad in ad_list:
#         NOview = summaryShit.objects.filter(adID=ad, date__range=(last_day, datetime.now()), view_or_click=1).count()
#         new_obj = summaryShit(adID=ad, date=last_day, count=NOview, view_or_click=1)
#         new_obj.save()
#         NOclick = summaryShit.objects.filter(adID=ad, date__range=(last_day, datetime.now()), view_or_click=0).count()
#         new_obj = summaryShit(adID=ad, date=last_day, count=NOclick, view_or_click=0)
#         new_obj.save()



