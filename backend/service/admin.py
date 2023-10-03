from django.contrib import admin

from .models import Site, Category, Subscribe


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display=['id','name','code']
    list_filter = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_filter = ('name',)