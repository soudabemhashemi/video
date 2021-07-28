from django.urls import path
from .views import crawl_aparat, ShowVideos, PlayVideo

app_name = "curl_video"
urlpatterns = [
    path('test1/', crawl_aparat, name="crawl-aparat"),
    path('show-videos/', ShowVideos.as_view(), name="video-list"),
    path('show-videos/play-video/<int:pk>/', PlayVideo.as_view(), name="play-video"),

]