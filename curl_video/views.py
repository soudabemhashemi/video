from django.db.models.aggregates import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .tasks import crawl_category
from .models import Video
from django.template import loader
from django.http import HttpResponse


SCROLL_LIMIT = 3
CATEGORY_LIMIT = 3


def crawl_aparat(request):
    driver = webdriver.Firefox()
    driver.get("https://www.aparat.com/")

    more_button = driver.find_element_by_xpath("//ul[@class='menu-list']/li[@class='menu-item-link menu-show-more']/a")
    more_button.click()

    categories_object = driver.find_elements_by_xpath( "//div[@id=2]/ul[@class='menu-list']/li[@class='menu-item-link']/a")

    categories = []

    for category in categories_object:
        categories.append({'name': category.text, 'url':category.get_attribute('href')})

    local_limit = CATEGORY_LIMIT
    if len(categories) < CATEGORY_LIMIT:
        local_limit = len(categories)

    for i in range(2, local_limit):
        crawl_category.delay(categories[i])
    
    driver.close()


def show_videos(request):
    categories = (Video.objects
        .values('category_name','sub_category_name')
        .annotate(dcount=Count('category_name', 'sub_category_name'))
        )
    
    videos = []
    for category in categories:
        videos.append(Video.objects.filter(category_name = category['category_name'], sub_category_name = category['sub_category_name']))
    
    print(videos)
    context = {
        'videos_list': videos
    }

    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


