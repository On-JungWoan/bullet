from django.db import models
from service.models import Site, Keyword
from post.models import Post

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#models의 baseUserManager를 상속받아 커스텀 userManager를 만듬. 이를 통해 user를 생성할 수 있다.
class UserManager(BaseUserManager):
    def create_user(self, username, password, email):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            is_superuser = 0,
            is_active = 1,
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    # Method Overriding
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username = username,
            password = password,
            email = email
        )
        user.is_superuser = 1
        user.is_staff = 1
        user.is_admin = 1
        user.save(using=self._db)
        return user
    
#user를 저장하는 테이블
class User(AbstractBaseUser, PermissionsMixin):
    #선언해주면 superuser와 admin이 관리할 수 있음
    objects = UserManager()

    #user 기본정보
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', null=True)
    #키워드, site개수
    keywordCount = models.IntegerField(default=0)
    siteCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #다대다 관계는 테이블이 추가되는데 자동으로 생성된다. 하지만 중간 테이블을 직접 만들면 추가적인 정보를 저장할 수 있다.
    keywords = models.ManyToManyField(Keyword, through='UserKeyword')
    sites = models.ManyToManyField(Site, through='UserSite')
    posts = models.ManyToManyField(Post, through='UserPost')
    
    USERNAME_FIELD = 'email'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['username']

    def __str__(self):
            """String for representing the Model object."""
            return self.username

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module(self, app_label):
        return True
    

    

    
#user가 등록한 site를 저장하는 테이블
class UserSite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.site.name
    
#user가 등록한 keyword를 저장하는 테이블
class UserKeyword(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.keyword.name
    
class UserPost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.post.title