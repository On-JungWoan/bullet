from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('post/<int:id>', views.findById, name='findById'),
    path('post/user/<int:user_id>', views.findByUserId, name='findByUserId'),
    path('post/create', views.create, name='create'),
]