from django.db import models
from service.models import Site, Keyword
# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=200)
    site = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    date = models.DateTimeField()
    created_at = models.DateTimeField()