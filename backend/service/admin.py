from django.contrib import admin

from .models import Keyword, Site, Category, Subscribe
# Register your models here.
admin.site.register(Keyword)
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Subscribe)