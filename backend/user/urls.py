from django.urls import path
from . import views

app_name='user'



urlpatterns = [ 
    path('signup/', views.UserViewSet.as_view({'post' : 'signup'})),
    path('login/', views.UserViewSet.as_view({'post' : 'login'})),
    path('check/', views.UserViewSet.as_view({'post' : 'checkEmail'})),
    
    path('<int:id>/', views.UserViewSet.as_view({'get' : 'findById'})),
]
