from django.db import models

# Create your models here.
def Subscribe(models):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField()

def Category(model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

def Site(model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

def Keyword(model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)