from rest_framework.test import APIClient, APITestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User


# class TestUserKeyword(APITestCase):
#     #user가 keyword를 추가하는 테스트
#     def test_userkeyword_create(self):
#         client = APIClient()
#         user = UserKeyword.objects.create(username="joo", password="1234", nickname="joo")

#         client.force_authenticate(user=user)
#         url = "/my_page/my_letter"
#         response = client.get(url)

#         self.assertEqual("올바른 편지 번호를 입력해주세요.", response.json()["detail"])
#         self.assertEqual(400, response.status_code)