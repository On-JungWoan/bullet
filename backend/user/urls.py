from django.urls import path
from . import views

app_name='user'



urlpatterns = [ 
    #쓰기용
    path('signup/', views.UserViewSet.as_view({'post' : 'signup'})),
    path('login/', views.UserViewSet.as_view({'post' : 'login'})),
    path('check/', views.UserViewSet.as_view({'post' : 'checkEmail'})),
    path('password/update/', views.UserViewSet.as_view({'post' : 'updatePassword'})),
    #읽기용
    path('<int:id>/', views.UserViewSet.as_view({'get' : 'findById'})),
    #user의 키워드, 사이트, 포스트 등록 url
    path('keyword/create/', views.UserKeywordViewSet.as_view({'post' : 'createUserKeyword'})),
    path('site/create/', views.UserSiteViewSet.as_view({'post' : 'createUserSite'})),
    #모든 유저가 등록한 키워드, 사이트, 포스트 검색 url
    # path('keyword/', views.UserKeywordViewSet.as_view({'get' : 'findAll'})),
    # path('site/', views.UserSiteViewSet.as_view({'get' : 'findAll'})),
    # path('post/', views.UserPostViewSet.as_view({'get' : 'findAll'})),
    #user의 키워드, 사이트, 포스트 검색 url
    path('keyword/', views.UserKeywordViewSet.as_view({'get' : 'findByUserId'})),
    path('site/', views.UserSiteViewSet.as_view({'get' : 'findByUserId'})),
    path('post/', views.UserPostViewSet.as_view({'get' : 'findByUserId'})),
]
