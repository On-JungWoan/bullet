from rest_framework import serializers
from .models import User, UserKeyword, UserSite, UserPost
from post.models import Post
from post.serializers import PostSerializer
from service.models import Keyword, Site
from service.serializers import KeywordSerializer, SiteSerializer, CategorySerializer
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
        return str(list(user.keywords.values_list('name',flat=True)))
    def get_sites(self, user):
        return str(list(user.sites.values_list('name',flat=True)))
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
class UserPostSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields =  ['id','posts']

    def create(self, validated_data, user):
        post_name = validated_data['keywords'][0]['name']
        post = Post.objects.get(name=post_name)
        user_keyword = UserKeyword.objects.get_or_create(user=user, post=post)
        return user_keyword
    
    def get_posts(self, user):
        return str(user.posts.values_list('name',flat=True))

#뉴스를 저장할 때 키워드와 사이트를 통해 저장하기 때문에 유저가 어떤 키워드를 구독했는지 알아야 한다.
class UserKeywordSerializer(serializers.ModelSerializer):
    keywords =serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','keywords']

    def create(self, validated_data, user):
        keyword_name = validated_data['keywords'][0]['name']
        keyword,created = Keyword.objects.get_or_create(name=keyword_name)
        user_keyword = UserKeyword.objects.get_or_create(user=user, keyword=keyword)
        return user_keyword
    
    def get_keywords(self, user):
        return str(list(user.keywords.values_list('name',flat=True)))

#유저가 어떤 사이트를 구독했는지 저장하는 클래스
class UserSiteSerializer(serializers.ModelSerializer):
    sites = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','sites']

    def create(self, validated_data, user):
        site_name = validated_data['sites']
        site = Site.objects.get(name=site_name)
        user_site = UserSite.objects.get_or_create(user=user, site=site)
        return user_site
    
    def get_sites(self, user):
        return str(list(user.sites.values_list('name',flat=True)))