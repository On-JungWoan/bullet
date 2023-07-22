from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
#로그인 관련
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
#유저 모델 호출
from .models import User
#데이터 전송 객체 호출
from . import serializers
#문서 관련
from drf_yasg.utils import swagger_auto_schema

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=serializers.SignupSerializer())
    def signup(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.SignupSerializer(data=request.data)
        #유저 모델에 저장
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.LoginSerializer())
    def login(self, request):
        email = request.data.get('email')#프론트에서 받아온 이메일
        password = request.data.get('password')#프론트에서 받아온 비밀번호
        
        #로그인 유효성 확인 로직이 들어갈 부분
        user = User.objects.filter(email=email).first()

        # 만약 username에 맞는 user가 존재하지 않는다면,
        if user is None:
            return Response(
                {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        # 비밀번호가 틀린 경우,
        #not check_password(password, user.password) -> 비밀번호가 틀린 경우
        if password != user.password:
            return Response(
                {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        # user가 맞다면,
        if user is not None:
            token = TokenObtainPairSerializer.get_token(user) # refresh 토큰 생성
            refresh_token = str(token) # refresh 토큰 문자열화
            access_token = str(token.access_token) # access 토큰 문자열화
            response = Response(
                {
                    "user": user.id,
                    "message": "login success",
                    "jwt_token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    },
                },
                status=status.HTTP_200_OK
            )

            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        else:
            return Response(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(request_body=serializers.CheckEmailSerializer())
    def checkEmail(self, request):
        email = request.data.get('email')
        return Response('check')

    @swagger_auto_schema(parameters = serializers.UserModelSerializer())
    def findById(self, id):
        user = User.objects.get(id=id)
        serializer = serializer(user)
        return Response(serializer)