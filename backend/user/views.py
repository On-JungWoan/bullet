from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
#로그인 관련
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import check_password
#유저 모델 호출
from .models import User, UserSite, UserKeyword, UserPost, Device
#데이터 전송 객체 호출
from . import serializers
#문서 관련
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from config.swagger import *

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=serializers.SignupSerializer())
    def signup(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.SignupSerializer(data=request.data)
        #유저 모델에 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.LoginSerializer(),
                         manual_parameters=auth_param)
    def login(self, request):
        jwt_auth = JWTAuthentication()
        user_and_token = jwt_auth.authenticate(request)
        print(user_and_token)
        if user_and_token is None:
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
            if check_password(user.password, request.data.get('password')):
                return Response(
                    {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST
                )

            # user가 맞다면,
            if user is not None:
                token = TokenObtainPairSerializer.get_token(user) # refresh 토큰 생성
                refresh_token = str(token) # refresh 토큰 문자열화
                access_token = str(token.access_token) # access 토큰 문자열화
                serializer = serializers.UserFullDataSerializer(user)
                headers = {"Authorization": "Bearer " + access_token, 
                        "Refresh-Token": refresh_token}
                return Response(serializer.data, headers=headers, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            auth_user, _ = user_and_token
            serializer = serializers.UserFullDataSerializer(auth_user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.CheckEmailSerializer())
    def checkEmail(self, request):
        result = serializers.CheckEmailSerializer(request)
        if result:
            return Response({"message": "이메일이 중복되지 않습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "이메일이 중복됩니다."}, status=status.HTTP_400_BAD_REQUEST)

    #@swagger_auto_schema(request_body={'id':1}, manual_parameters=auth_param)
    def get(self, id):
        user = User.objects.get(id=id)
        serializer = self.serializer(user)
        return Response(serializer)
    
    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #@swagger_auto_schema(request_body={'password':'1234'}, manual_parameters=auth_param)
    def updatePassword(self, request):
        user = User.objects.get(id = request.user)
        #비밀번호가 동일하다면?
        if check_password(user.password, request.data.get('password')):
            user.password = request.data.get('password')
            user.save(update_fields=['password'])
            return Response({"message": "성공적으로 비밀번호를 변경하였습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "현재 비밀번호가 일치하지 않습니다."},status=status.HTTP_400_BAD_REQUEST)


#-----------유저별 키워드, 사이트, 포스트 관련-------
class UserSiteViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    jwt_auth = JWTAuthentication()  
    @swagger_auto_schema(request_body=serializers.SaveUserSiteSerializer, manual_parameters=auth_param)
    def createUserSite(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.SaveUserSiteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(validated_data=serializer.validated_data,user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "등록되지 않은 사이트입니다."},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "확인되지않은 유저입니다."},status=status.HTTP_401_UNAUTHORIZED)

    def list(self, request):
            serializer = self.serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(manual_parameters=auth_param)
    def get(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.GetUserSiteSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"인증되지 않은 유저입니다."}
                        ,status=status.HTTP_401_UNAUTHORIZED)

    @swagger_auto_schema(request_body=serializers.SaveUserSiteSerializer, manual_parameters=auth_param)
    def delete(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.SaveUserSiteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.delete(validated_data=serializer.validated_data, user = user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({"message":"등록되지 않은 사이트입니다."},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "인증되지않은 유저입니다."},status=status.HTTP_401_UNAUTHORIZED)
    

class UserKeywordViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    jwt_auth = JWTAuthentication()

    @swagger_auto_schema(request_body=serializers.SaveUserKeywordSerializer, manual_parameters=auth_param)
    def createUserKeyword(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.SaveUserKeywordSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(validated_data=serializer.validated_data,user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"잘못된 키워드입니다."},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"인증되지 않은 유저입니다."}
                        ,status=status.HTTP_401_UNAUTHORIZED)


    def list(self, request):
            serializer = self.serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(manual_parameters=auth_param)
    def get(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.GetUserKeywordSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"인증되지 않은 유저입니다."}
                        ,status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.SaveUserKeywordSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.delete(validated_data=serializer.validated_data,user=user)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"잘못된 키워드 요청입니다."},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"인증되지 않은 유저입니다."}
                        ,status=status.HTTP_401_UNAUTHORIZED)
        

class UserPostViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    jwt_auth = JWTAuthentication()

    @swagger_auto_schema(request_body=serializers.SaveUserPostSerializer, manual_parameters=auth_param)
    def createUserPost(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.SaveUserPostSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(validated_data=serializer.validated_data,user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema()
    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(manual_parameters=auth_param)
    def get(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.GetUserPostSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class UserIntervalViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    jwt_auth = JWTAuthentication()
    
    @swagger_auto_schema(request_body=serializers.SetIntervalSerializer, manual_parameters=auth_param)
    def setInterval(self, request):
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            serializer = serializers.SetIntervalSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(validated_data=serializer.validated_data,user=user)
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"인증되지 않은 유저입니다."}
                        ,status=status.HTTP_401_UNAUTHORIZED)
        
class UserFcmTokenViewSet(viewsets.GenericViewSet):
    queryset = Device.objects.all()
    @swagger_auto_schema(request_body=serializers.SaveFcmTokenSerializer)
    def saveFcmToken(self, request):
        serializer = serializers.SaveFcmTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(validated_data=serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)