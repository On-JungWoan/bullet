from rest_framework import serializers
from .models import User, UserKeyword, UserSite, UserPost, Device
from post.models import Post
from post.serializers import PostSerializer
from service.models import Site, Category

#유저의 모든 정보를 저장하는 클래스
class UserFullDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    keywordCount = serializers.IntegerField()
  #  keywords = serializers.SerializerMethodField()
    announce = serializers.SerializerMethodField()
    news = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)


    # def get_keywords(self, user):
    #     return list(user.site.keywords.values_list('name',flat=True))
    def get_announce(self, user):
        category = 1
        listfield = []
        sites_in_category = user.sites.filter(category=category)
        # for site in sites_in_category:
        keywords = UserKeyword.objects.filter(usersite__user_id = user.id, usersite__site_id=sites_in_category[0].id).values_list('name', flat=True)
        listfield.append({"sites":sites_in_category.values_list('name', flat=True)})
        listfield.append({"keysords":keywords})

        print(listfield)
        return listfield
    def get_news(self, user):
        category = 2
        listfield = []
        sites_in_category = user.sites.filter(category=category)
        # for site in sites_in_category:
        #     keywords = UserKeyword.objects.filter(usersite__user_id = user.id, usersite__site_id=site.id).values_list('name', flat=True)
        #     listfield.append({site.name:keywords})
        keywords = UserKeyword.objects.filter(usersite__user_id = user.id, usersite__site_id=sites_in_category[0].id).values_list('name', flat=True)
        listfield.append({"sites":sites_in_category.values_list('name', flat=True)})
        listfield.append({"keysords":keywords})
        return listfield
    def get_jobs(self, user):
        category = 3
        listfield = []
        sites_in_category = user.sites.filter(category=category)
        keywords = UserKeyword.objects.filter(usersite__user_id = user.id, usersite__site_id=sites_in_category[0].id).values_list('name', flat=True)
        listfield.append({"sites":sites_in_category.values_list('name', flat=True)})
        listfield.append({"keysords":keywords})
        return listfield

#유저가 어떤 키워드를 구독했는지 저장하는 클래스.
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
            instance.set_password(password)
            instance.save()
        return instance

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class CheckEmailSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['email']
    def get_email(self, email):
        user = User.objects.filter(email=email).first()
        if user is None:
            return True
        else:
            return False
    


#-----------------유저와 관계가 있는 모델 시리얼라이저---------
#유저와 포스트 사이에서 유저에게 전송될 뉴스를 저장하는 클래스
class GetUserPostSerializer(serializers.Serializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields =  ['posts']

    def get_posts(self, user):
        return str(user.posts.values_list('title',flat=True))

#뉴스를 저장할 때 키워드와 사이트를 통해 저장하기 때문에 유저가 어떤 키워드를 구독했는지 알아야 한다.
class GetUserKeywordSerializer(serializers.ModelSerializer):
    keywords = serializers.SerializerMethodField()

    class Meta:
        model = UserKeyword
        fields = ('name','site')

    def get_keywords(self, user):
        return list(UserKeyword.objects.filter(site__user_id = user.id).values_list('name',flat=True))

#유저가 어떤 사이트를 구독했는지를 확인하는 클래스
class GetUserSiteSerializer(serializers.Serializer):
    announce = serializers.SerializerMethodField()
    news = serializers.SerializerMethodField()
    jobs = serializers.SerializerMethodField()
    
    def get_announce(self, user):
        category = 1
        sites_in_category = user.sites.filter(category=category).values_list('name', flat=True)
        return sites_in_category
    def get_news(self, user):
        category = 2
        sites_in_category = user.sites.filter(category=category).values_list('name', flat=True)
        return sites_in_category
    def get_jobs(self, user):
        category = 3
        sites_in_category = user.sites.filter(category=category).values_list('name', flat=True)
        return sites_in_category
    
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
    category = serializers.CharField()
    keywords = serializers.ListField(child=serializers.CharField())

    def save(self, validated_data, user):
        print(validated_data)
        if len(validated_data['keywords']) > 5:
            return serializers.ValidationError("키워드는 5개까지만 등록할 수 있습니다.")
        
        category = Category.objects.get(name=validated_data['category'])
        print(category)
        
        usersites = UserSite.objects.filter(user=user, site__category=category) 
        print(usersites)
        UserKeyword.objects.filter(usersite__in = usersites).delete()  # 해당 유저의 모든 키워드 삭제
        print("Asdfasdfadf")
        keywords = validated_data['keywords']
        for usersite in usersites:
            user_keyword = [UserKeyword.objects.get_or_create(usersite=usersite, name=keyword) for keyword in keywords]
        # YourModel 객체들을 일괄 저장
        return user_keyword
    
    def delete(self, validated_data, user):
        keywords = validated_data['keywords']
        UserKeyword.objects.filter(site__user=user, keyword=keywords).delete()
        
#유저가 어떤 사이트를 구독했는지 저장하는 클래스
class SaveUserSiteSerializer(serializers.Serializer):
    sites = serializers.ListField(child=serializers.CharField())

    def save(self, validated_data, user):
        if len(validated_data['sites']) > 5:
            return serializers.ValidationError("사이트는 5개까지만 등록할 수 있습니다.")
        UserSite.objects.filter(user=user).delete()  # 해당 유저의 모든 사이트 삭제
        sites = validated_data['sites']
        sites = Site.objects.filter(name__in=sites)
        print(sites)
        if len(sites) == 0:
            print("asdfsf")
            return serializers.ValidationError("존재하지 않는 사이트입니다.")
        
        user_site = [UserSite.objects.get_or_create(user=user, site=site) for site in sites]
        return user_site
    
    def delete(self, validated_data, user):
        for category in validated_data:
            sites = Site.objects.filter(name__in = validated_data.get(category))
            UserSite.objects.filter(user=user, site__in=sites).delete()

class SetIntervalSerializer(serializers.Serializer):
    interval = serializers.IntegerField()
    def save(self, validated_data, user):
        user.interval = validated_data['interval']
        user.save(update_fields=['interval'])
        return user.interval
    
class SaveFcmTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    def save(self, validated_data, user):
        device = Device.objects.get_or_create(user=user)[0]
        device.fcmtoken = validated_data['token']
        device.save()
        return device.fcmtoken