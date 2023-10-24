from django.contrib import admin

from .models import User, UserKeyword, UserSite
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','email','keywordCount','siteCount']

@admin.register(UserKeyword)
class UserKeywordAdmin(admin.ModelAdmin):
    list_display=['id','user','name','category']
    list_filter = ('name','category')

@admin.register(UserSite)
class UserSiteAdmin(admin.ModelAdmin):
    list_display=['id','user','site']
    list_filter = ('user','site')

