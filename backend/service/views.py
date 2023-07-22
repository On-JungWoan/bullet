from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from user.serializers import UserSiteSerializer, UserKeywordSerializer
class SiteViewSet(viewsets.ViewSet):
    def createUserSite():
        pass
class KeywordViewSet(viewsets.ViewSet):
    def createUserKeyword():
        pass

