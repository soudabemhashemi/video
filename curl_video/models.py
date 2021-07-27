from django.db import models
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100, blank=False)
    category_name = models.CharField(max_length=100)
    sub_category_name = models.CharField(max_length=100)
    url = models.URLField(blank=False)
    download_link = models.URLField()
    tag = models.CharField(max_length=100)
    cover = models.ImageField(default='index.jpeg', upload_to="media/%y")
    video = models.FileField(default="temp.mp4")