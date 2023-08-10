from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # 요청 데이터에서 refresh token 추출
        refresh_token = request.data.get('refresh') 
        if not refresh_token:
            raise AuthenticationFailed('No refresh token provided')
        try:
            refresh = RefreshToken(refresh_token)  # RefreshToken 객체 생성
            access_token = str(refresh.access_token)  # 새로운 Access Token 생성
            #refresh에서 유저정보를 가져옴
            user = refresh.get('user')
            print(user)
            #유저 인증 로직 필요한가?

            # 새로운 Access Token과 사용자 정보를 반환
            headers = {"Authorization": "Bearer " + access_token, 
                        "Refresh-Token": refresh_token}
            return Response(headers=headers, status=status.HTTP_200_OK)
        
        except AuthenticationFailed:
            raise AuthenticationFailed('Invalid refresh token')