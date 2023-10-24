from django.shortcuts import render
#REST API
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
#models
from .models import Post
from user.models import User, UserKeyword
from .serializers import PostSerializer
#유저는 데이터를 조회 이외에는 하지 않는다. 유저는 데이터 조회를 위해 토큰 소유를 인증해야 한다.
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from config.swagger import auth_param
#쿼리용 import
from itertools import product
from django.db.models import Q
#프론트에서 id를 통해 post를 검색
class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    jwt_auth = JWTAuthentication()

    def get(request):
        id=request.GET.get('id')
        post=Post.objects.get(id=id)
        return Response(post)

    #프론트엔드에서 user의 id를 통해 그 유저가 등록한 뉴스를 검색할 수 있음
    @swagger_auto_schema(manual_parameters=auth_param)
    def list(self, request):
        # 유저 객체 가져오기
        user_and_token = self.jwt_auth.authenticate(request)
        if user_and_token is not None:
            user, _ = user_and_token
            user = User.objects.get(id=user.id)
            # 해당 유저와 관련된 뉴스 인스턴스들을 가져오되, 키워드 정보도 함께 로드하기
            keywords = list(UserKeyword.objects.filter(user=user).values_list('name',flat=True))
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
        else:
            return Response({"message":"인증되지 않은 유저입니다."}
                        ,status=status.HTTP_401_UNAUTHORIZED)