from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
#로그인 관련
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
#유저 모델 호출
from .models import User, UserSite, UserKeyword, UserPost
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
            serializer = serializers.UserFullDataSerializer(user)
            headers = {"Authorization": "Bearer " + access_token, 
                       "Refresh-Token": refresh_token}
            return Response(serializer.data, headers=headers, status=status.HTTP_200_OK)
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
        serializer = self.serializer(user)
        return Response(serializer)

    @swagger_auto_schema(request_body=serializers.UserModelSerializer())
    def updatePassword(self, request):
        user = User.objects.get(id = request.user)
        #비밀번호가 동일하다면?
        if check_password(user.password, request.data.get('password')):
            user.password = request.data.get('password')
            user.save()
            return Response({"message": "성공적으로 비밀번호를 변경하였습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "비밀번호가 일치하지 않습니다."},status=status.HTTP_400_BAD_REQUEST)

#-----------유저별 키워드, 사이트, 포스트 관련-------
class UserSiteViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer = serializers.UserSiteSerializer

    @swagger_auto_schema(request_body=serializer)
    def createUserSite(self, request):
        serializer = self.serializer(data = request.data)
        if serializer.is_valid():
            user = request.user
            serializer.save(validated_data=request.data, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def findAll(self, request):
            serializer = self.serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def findByUserId(self, request):
        user = request.user
        userSite = UserSite.objects.filter(user=user)
        serializer = self.serializer(userSite, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserKeywordViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer = serializers.UserKeywordSerializer

    @swagger_auto_schema(request_body=serializer)
    def createUserKeyword(self, request):
        serializer = self.serializer(data = request.data)
        if serializer.is_valid():
            user = request.user
            serializer.create(validated_data=request.data, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def findAll(self, request):
            serializer = self.serializer(self.queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def findByUserId(self, request):
        user = request.user
        userKeyword = UserKeyword.objects.filter(user=user)
        serializer = self.serializer(userKeyword, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserPostViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer = serializers.UserPostSerializer
    
    @swagger_auto_schema(request_body=serializer)
    def createUserPost(self, request):
        serializer = self.serializer(data = request.data)
        if serializer.is_valid():
            user = request.user
            serializer.create(validated_data=request.data, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema()
    def findAll(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def findByUserId(self, request):
        user = request.user
        userPost = UserPost.objects.filter(user=user)
        serializer = self.serializer(userPost, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)