from django.contrib import admin

from .models import User, UserKeyword, UserSite
# Register your models here.

admin.site.register(User)
admin.site.register(UserKeyword)
admin.site.register(UserSite)