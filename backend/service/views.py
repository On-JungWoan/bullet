from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.response import Response
#model&serializer import
from .models import Category, Site
from .serializers import CategorySerializer, SiteSerializer

#문서 관련
from drf_yasg.utils import swagger_auto_schema

class CategoryViewSet(viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def findAll(self, request):
        categories = self.queryset
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SiteViewSet(viewsets.GenericViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    @swagger_auto_schema(responses={200: SiteSerializer(many=True)})
    def findByCategory(self, request, categoryId):
        sites = Site.objects.filter(category = categoryId)
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

