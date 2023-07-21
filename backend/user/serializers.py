from rest_framework import serializers
from .models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    posts = Post.PostSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        posts = validated_data.pop('posts')
        user = Post.objects.create(**validated_data)
        for post in posts:
            post, _ = Post.objects.get_or_create(**post)
            user.post.add(post)
        return user