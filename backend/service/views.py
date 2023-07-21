from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def index(request):
    return Response("연결되었습니다.")

@api_view(["POST"])
def createKeyword(request):
    return Response("createKeyword")

@api_view(["GET"])
def keywordFindByUserId(request):
    return Response("keywordFindByUserId")

@api_view(["GET"])
def keywordFindById(request):
    return Response("keywordFindById")

@api_view(["POST"])
def createSite(request):
    return Response("createSite")

@api_view(["GET"])
def siteFindByUserId(request):
    return Response("siteFindByUserId")

@api_view(["GET"])
def siteFindById(request):
    return Response("siteFindById")

@api_view(["POST"])
def createCategory(request):
    return Response("createCategory")

@api_view(["GET"])
def categoryFindByUserId(request):
    return Response("categoryFindByUserId")

@api_view(["GET"])
def categoryFindById(request):
    return Response("categoryFindById")