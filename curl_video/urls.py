from django.urls import path
from .views import crawl_aparat, show_videos

urlpatterns = [
    path('test1/', crawl_aparat),
    path('show-videos/', show_videos),
]