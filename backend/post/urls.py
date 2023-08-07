from django.urls import path,include
from . import views


app_name='post'


urlpatterns = [ 
    path('<int:id>/', views.PostViewSet.as_view({'get' : 'findById'})),
    path('user/', views.PostViewSet.as_view({'get' : 'findByUserId'})),
]
