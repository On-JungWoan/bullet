from django.shortcuts import render
#REST API
from rest_framework.response import Response
#models
from .models import Post
from user.models import User, UserPost
#유저는 데이터를 조회 이외에는 하지 않는다. 유저는 데이터 조회를 위해 토큰 소유를 인증해야 한다.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt.authentication import JSONWebTokenAuthentication
#프론트에서 id를 통해 post를 검색
@api_view(['GET'])
def findById(request):
    id=request.GET.get('id')
    post=Post.objects.get(id=id)
    return Response(post)

#프론트엔드에서 user의 id를 통해 그 유저가 등록한 뉴스를 검색할 수 있음
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
#@authentication_classes((JSONWebTokenAuthentication,))
def findByUserId(request):
    user_id=request.GET.get('user_id')
    # 유저 객체 가져오기
    user = User.objects.get(id=user_id)
    # 해당 유저와 관련된 뉴스 인스턴스들을 가져오되, 키워드 정보도 함께 로드하기
    posts = UserPost.objects.filter(user=user).prefetch_related('post')
    return Response(posts)

# Create your views here.
