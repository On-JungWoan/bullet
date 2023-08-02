from rest_framework import serializers
from .models import User, UserKeyword, UserSite, UserPost
from post.models import Post
from post.serializers import PostSerializer
from service.models import Keyword, Site
from service.serializers import KeywordSerializer, SiteSerializer, CategorySerializer
import json
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

#유저의 모든 정보를 저장하는 클래스
class UserFullDataSerializer(serializers.ModelSerializer):
    keywords = serializers.SerializerMethodField()
    sites = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','email','username','keywordCount','keywords','sites')

    def get_keywords(self, user):
        return list(user.keywords.values_list('name',flat=True))
    def get_sites(self, user):
        return list(user.sites.values_list('name',flat=True))
#유저가 어떤 키워드를 구독했는지 저장하는 클래스.
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class CheckEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


#-----------------유저와 관계가 있는 모델 시리얼라이저---------
#유저와 포스트 사이에서 유저에게 전송될 뉴스를 저장하는 클래스
class GetUserPostSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields =  ['posts']

    def get_posts(self, user):
        return str(user.posts.values_list('name',flat=True))

#뉴스를 저장할 때 키워드와 사이트를 통해 저장하기 때문에 유저가 어떤 키워드를 구독했는지 알아야 한다.
class GetUserKeywordSerializer(serializers.ModelSerializer):
    keywords = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('keywords',)

    def get_keywords(self, user):
        return list(user.keywords.values_list('name',flat=True))

#유저가 어떤 사이트를 구독했는지 저장하는 클래스
class GetUserSiteSerializer(serializers.ModelSerializer):
    sites = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('sites',)
    
    def get_sites(self, user):
        return list(user.sites.values_list('name',flat=True))
    
class SaveUserPostSerializer(serializers.Serializer):
    posts = serializers.ListField(child=serializers.CharField())

    def save(self, validated_data, user):
        posts = validated_data['posts']
        posts_create = [Post.objects.get_or_create(name=post)[0] for post in posts]
        user_post = [UserPost.objects.get_or_create(user=user, post=post) for post in posts_create]
        # YourModel 객체들을 일괄 저장
        return user_post

#뉴스를 저장할 때 키워드와 사이트를 통해 저장하기 때문에 유저가 어떤 키워드를 구독했는지 알아야 한다.
class SaveUserKeywordSerializer(serializers.Serializer):
    keywords = serializers.ListField(child=serializers.CharField())

    def save(self, validated_data, user):
        print(validated_data)
        keywords = validated_data['keywords']
        keywords_create = [Keyword.objects.get_or_create(name=keyword)[0] for keyword in keywords]
        print(keywords_create)
        user_keyword = [UserKeyword.objects.get_or_create(user=user, keyword=keyword) for keyword in keywords_create]
        # YourModel 객체들을 일괄 저장
        return user_keyword

#유저가 어떤 사이트를 구독했는지 저장하는 클래스
class SaveUserSiteSerializer(serializers.Serializer):
    sites = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data, user):
        sites = validated_data['sites']
        sites_create = [Site.objects.get_or_create(name=site)[0] for site in sites]
        user_site = [UserSite.objects.get_or_create(user=user, site=site) for site in sites_create]
        return user_site