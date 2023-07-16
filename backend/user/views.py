from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#로그인 관련
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
#유저 모델 호출
from .models import User

# Create your views here.
@api_view(["GET","POST"])
def signup(request):
    return Response("Hello, world. You're at the users index.")

@api_view(["POST"])
def login(request):
    email = request.POST.get('email')#프론트에서 받아온 이메일
    password = request.POST.get('password')#프론트에서 받아온 비밀번호
    
    #로그인 유효성 확인 로직이 들어갈 부분
    user = User.objects.filter(username=email).first()

    # 만약 username에 맞는 user가 존재하지 않는다면,
    if user is None:
        return Response(
            {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
        )

    # 비밀번호가 틀린 경우,
    if not check_password(password, user.password):
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

@api_view(["POST"])
def check(request):
    return Response('check')

@api_view(["GET"])
def findById(request):
    return Response('findById')