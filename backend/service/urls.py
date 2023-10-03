from django.urls import path
from . import views

app_name='service'

urlpatterns = [
    path('category/', views.CategoryViewSet.as_view({'get' : 'findAll'}), name='category'),
    path('category/<int:categoryId>/site', views.SiteViewSet.as_view({'get' : 'findByCategory'}), name='site'),
]