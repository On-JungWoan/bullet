from django.urls import path
from . import views

app_name='user'



urlpatterns = [ 
    #쓰기용
    path('signup/', views.UserViewSet.as_view({'post' : 'signup'})),
    path('login/', views.UserViewSet.as_view({'post' : 'login'})),
    path('check/', views.UserViewSet.as_view({'post' : 'checkEmail'})),
    #읽기용
    path('<int:id>/', views.UserViewSet.as_view({'get' : 'findById'})),
    #user의 키워드 및 사이트 등록 url
    path('keyword/create', views.UserKeywordViewSet.as_view({'post' : 'createKeyword'})),
    path('site/create', views.UserSiteViewSet.as_view({'post' : 'createSite'})),
]
