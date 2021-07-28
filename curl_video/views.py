from django.db.models.aggregates import Count
from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .tasks import crawl_category
from .models import Video, CategoryCatalog
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

SCROLL_LIMIT = 3
CATEGORY_LIMIT = 4


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


class ShowVideos(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories_object = (CategoryCatalog.objects
        .values('category_name')
        .annotate(dcount=Count('category_name'))
        )

        categories = []
        for category in categories_object:
            categories.append(CategoryCatalog.objects.filter(category_name = category['category_name']))

        videos = []
        for category in categories:
            for sub_category in category:
                videos.append(sub_category.my_videos.all())
        
        context['videos_list'] = videos
        context['category_list'] = categories

        return context


# class PlayVideo(TemplateView):
#     template_name = "play-video.html"

# def PlayVideo(request, video_id):
#     return HttpResponse(video_id)

class PlayVideo(TemplateView):
    template_name = "play-video.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = Video.objects.get(pk=kwargs['pk'])
        print(video.title)
        context['video'] = video
        return context