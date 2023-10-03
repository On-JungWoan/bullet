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
    path('<int:id>/', views.UserViewSet.as_view({'get' : 'get'})),
    path('', views.UserViewSet.as_view({'get' : 'list'})),

    #user의 키워드, 사이트, 포스트 등록 url
    path('keyword/create/', views.UserKeywordViewSet.as_view({'post' : 'createUserKeyword'})),
    path('site/create/', views.UserSiteViewSet.as_view({'post' : 'createUserSite'})),
    #user의 키워드, 사이트, 포스트 검색 url
    path('keyword/', views.UserKeywordViewSet.as_view({'get' : 'get'})),
    path('site/', views.UserSiteViewSet.as_view({'get' : 'get'})),
    #path('post/', views.UserPostViewSet.as_view({'get' : 'findByUserId'})),
    #user의 키워드, 사이트, 포스트 삭제 url
    path('keyword/delete/', views.UserKeywordViewSet.as_view({'post' : 'delete'})),
    path('site/delete/', views.UserSiteViewSet.as_view({'post' : 'delete'})),
    #간격 설정
    path('interval/', views.UserIntervalViewSet.as_view({'post' : 'setInterval'})),
    #fcm token
    path('fcm/', views.UserFcmTokenViewSet.as_view({'post' : 'saveFcmToken'})),
]
