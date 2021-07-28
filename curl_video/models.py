from django.db import models


class CategoryCatalog(models.Model):
    category_name = models.CharField(max_length=100)
    sub_category_name = models.CharField(max_length=100)


class Video(models.Model):
    title = models.CharField(max_length=100, blank=False)
    sub_category_id = models.ForeignKey(CategoryCatalog, on_delete=models.CASCADE, related_name="my_videos")
    url = models.URLField(blank=False)
    download_link = models.URLField()
    tag = models.CharField(max_length=100)
    cover = models.ImageField(default='index.jpeg', upload_to="media/%y")
    video = models.FileField(default="temp.mp4")

