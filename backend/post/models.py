from django.db import models
from service.models import Site
# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    url = models.CharField(max_length=200, unique=True)
    site = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    date = models.DateTimeField()
    created_at = models.DateTimeField()

class Notification(models.Model):
    time = models.DateTimeField()
    interval_minutes = models.PositiveIntegerField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    