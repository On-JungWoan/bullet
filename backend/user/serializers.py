from rest_framework import serializers
from .models import User, UserKeyword, UserSite, UserPost
from post.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
            keywordCount=validated_data['keywordCount']
        )
        return user

#유저와 포스트 사이에서 유저에게 전송될 뉴스를 저장하는 클래스
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'

    def create(self, validated_data):
        userPost = UserPost.objects.create(
            user=validated_data['user'],
            post=validated_data['post']
        )
        return userPost
#유저가 어떤 키워드를 구독했는지 저장하는 클래스.
#뉴스를 저장할 때 키워드와 사이트를 통해 저장하기 때문에 유저가 어떤 키워드를 구독했는지 알아야 한다.
class UserKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKeyword
        fields = '__all__'

    def create(self, validated_data):
        userKeyword = UserKeyword.objects.create(
            user=validated_data['user'],
            keyword=validated_data['keyword']
        )
        return userKeyword

#유저가 어떤 사이트를 구독했는지 저장하는 클래스
class UserSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSite
        fields = '__all__'

    def create(self, validated_data):
        userSite = UserSite.objects.create(
            user=validated_data['user'],
            site=validated_data['site']
        )
        return userSite