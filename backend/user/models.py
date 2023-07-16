from django.db import models
from service.models import Site, Keyword
from post.models import Post

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#models의 baseUserManager를 상속받아 커스텀 userManager를 만듬. 이를 통해 user를 생성할 수 있다.
# class UserManager(BaseUserManager):    
   
#    use_in_migrations = True    
   
#    def create_user(self, email, password):        
#        if not email:            
#            raise ValueError('must have user email')
#        if not password:            
#            raise ValueError('must have user password')
#        user = self.model(            
#            email=self.normalize_email(email),             
#        )        
#        user.set_password(password)        
#        user.save(using=self._db)        
#        return user

#    def create_superuser(self, email, password):        
#        user = self.create_user(            
#            email = self.normalize_email(email),                      
#            password=password        
#        )
#        user.is_admin = True
#        user.is_superuser = True
#        user.save(using=self._db)
#        return user
    
#user를 저장하는 테이블
class User(AbstractBaseUser):
    #선언해주면 superuser와 admin이 관리할 수 있음
    #objects = UserManager()

    #user의 테이블 속성들 정의
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    keywordCount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #다대다 관계는 테이블이 추가되는데 자동으로 생성된다. 하지만 중간 테이블을 직접 만들면 추가적인 정보를 저장할 수 있다.
    keywords = models.ManyToManyField(Keyword, through='UserKeyword')
    sites = models.ManyToManyField(Site, through='UserSite')
    posts = models.ManyToManyField(Post, through='UserPost')
    
    def __str__(self):
            """String for representing the Model object."""
            return self.name
    
    #권한 확인 부분. admin이나 superuser인지 확인하는 부분. 구현x
    # @property
    # def is_staff(self):
    #     return self.is_admin
    
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
        return self.keyword
    
class UserPost(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.post.title