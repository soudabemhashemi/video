from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "category_name", "sub_category_name", "url", "download_link", "tag"]