from django.contrib import admin
from .models import Post, Notification

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','keyword','site','created_at']
    list_filter = ('title','keyword','site','created_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=['id','time','interval_minutes','user']
    list_filter = ('time','interval_minutes','user')