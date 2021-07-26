from django.urls import path
from .views import crawl_aparat

urlpatterns = [
    path('test1/', crawl_aparat)
]