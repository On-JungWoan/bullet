from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#jwt token. 데코레이터와 함께 작동함.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#api를 한번에 볼 수 있게 해주는 swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   #admin url
   path('admin/', admin.site.urls),#admin url
   path('api-auth/',include('rest_framework.urls')),#api-auth url
   #토큰 관련 검증 url
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   #기능 url
   path('service/', include('service.urls')),#서비스 로직 관련 urls.py를 포함시킨다.
   path('user/', include('user.urls')),#유저관련 urls.py를 포함시킨다.
   path('post/', include('post.urls')),#post관련 urls.py를 포함시킨다.

   #swagger view
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
