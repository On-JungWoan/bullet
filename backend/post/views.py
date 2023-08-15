from django.shortcuts import render
#REST API
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
#models
from .models import Post
from user.models import User, UserPost
from .serializers import PostSerializer
#유저는 데이터를 조회 이외에는 하지 않는다. 유저는 데이터 조회를 위해 토큰 소유를 인증해야 한다.
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
#from rest_framework_simplejwt.authentication import JSONWebTokenAuthentication
from user.models import UserSite, UserKeyword
from django.db.models import Q
from itertools import product
#쿼리용 import

#프론트에서 id를 통해 post를 검색
class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    jwt_auth = JWTAuthentication()

    def findById(request):
        id=request.GET.get('id')
        post=Post.objects.get(id=id)
        return Response(post)

    #프론트엔드에서 user의 id를 통해 그 유저가 등록한 뉴스를 검색할 수 있음
    def findByUserId(self, request):
        # 유저 객체 가져오기
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            user = User.objects.get(id=user.id)
            # 해당 유저와 관련된 뉴스 인스턴스들을 가져오되, 키워드 정보도 함께 로드하기
            keywords = list(user.keywords.values_list('name',flat=True))
            sites = list(user.sites.values_list('code', flat=True))

            q_objects = Q()

            # 모든 조합을 생성하여 Q 객체에 추가. 형식 : Q(keyword=keyword1, site=site1) 또는 Q(keyword=keyword1, site=site2) 또는 ...
            for keyword, site in product(keywords, sites):
                q_objects |= Q(keyword=keyword, site=site)
            # post들을 Q object로 생성하고 한번에 필터링
            posts = Post.objects.filter(q_objects)
            posts_serializer = PostSerializer(posts, many=True)
            print(posts_serializer.data)
            return Response(posts_serializer.data)

# @api_view(['POST'])
# def create(request):
#     #프론트에서 받은 데이터
#     serializer = PostSerializer(data=request.data)
#     #post 인스턴스 저장
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
# Create your views here.
