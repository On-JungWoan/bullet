from django.contrib import admin

from .models import User, UserKeyword, UserSite
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','email','interval']
    list_filter = ('username','email','interval')

@admin.register(UserKeyword)
class UserKeywordAdmin(admin.ModelAdmin):
    list_display=['id','name','usersite']
    list_filter = ('name','usersite')

@admin.register(UserSite)
class UserSiteAdmin(admin.ModelAdmin):
    list_display=['id','user','site']
    list_filter = ('user','site')

