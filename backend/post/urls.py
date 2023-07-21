from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

app_name='post'

# viewset은 router를 사용하여 URL을 관리
router = DefaultRouter()  
router.register(r'post/<int:id>', views.PostModelViewSet)
router.register(r'post/user/<int:user_id>', views.PostModelViewSet)
router.register(r'post/create', views.PostModelViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]
