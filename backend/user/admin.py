from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User
# Register your models here.
class UserAdmin(BaseUserAdmin):
    # 관리자 페이지에서 유저 생성, 유저 수정시 사용할 폼을 추가할 수 있지만 구현을 안함
    #    form = UserChangeForm
    #    add_form = UserCreationForm

    # 화면에 보여질 유저 모델의 필드를 설정한다.
    list_display = ['email']

    fieldsets = (
    ['email', 'password']
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'organization', 'password1', 'password2'),
    #     }),
    # )
    search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ()

admin.site.register(User, UserAdmin)