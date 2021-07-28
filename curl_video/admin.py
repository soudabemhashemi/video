from django.contrib import admin
from .models import Video, CategoryCatalog

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "sub_category_id", "url", "download_link", "tag"]


@admin.register(CategoryCatalog)
class CategoryCatalogAdmin(admin.ModelAdmin):
    list_display = ["category_name", "sub_category_name"]