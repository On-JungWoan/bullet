from django.urls import path
from . import views

app_name='service'

urlpatterns = [
    path('index/', views.index, name='index'),
    #keyword 관련 요청
    path('keyword/create', views.createKeyword, name='createKeyword'),
    path('keyword/user/<int:user_id>', views.keywordFindByUserId, name='findByUserId'),
    path('keyword/<int:id>', views.keywordFindById, name='findById'),
    #site 관련 요청
    path('site/create', views.createSite, name='createSite'),
    path('site/user/<int:user_id>', views.siteFindByUserId, name='findByUserId'),
    path('site/<int:id>', views.siteFindById, name='findById'),
    #category 관련 요청
    path('category/create', views.createCategory, name='createCategory'),
    path('category/user/<int:user_id>', views.categoryFindByUserId, name='findByUserId'),
    path('category/<int:id>', views.categoryFindById, name='findById'),
]