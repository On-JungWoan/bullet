from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET","POST"])
def signup(request):
    return Response("Hello, world. You're at the users index.")

@api_view(["POST"])
def login(request):
    return Response("login")

@api_view(["POST"])
def check(request):
    return Response('check')

@api_view(["GET"])
def findById(request):
    return Response('findById')