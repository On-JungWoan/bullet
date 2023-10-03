from rest_framework.test import APIClient, APITestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User

# class SignUpUserTest(APITestCase):
# 	def test_registration(self):
# 		url = reverse("user_view")
# 		user_data = {
# 		"username" : "test",
# 		"fullname" : "테스터",
# 		"email" : "test@testuser.com",
# 		"password" : "password",
# 		}
# 		response = self.client.post(url, user_data)
# 		self.assertEqual(response.status_code, 200)
		
# class LoginUserTest(APITestCase):
# 	def setUp(self):
# 		#입력데이터1 - 옳은 데이터
# 		self.data = {"username" : "test", "password": "password"}
#         self.user = User.objects.create("test", "password")

# 	def test_login(self):
# 		response = self.client.post(reverse('token_obtain_pair'), self.data)
# 		self.assertEqual(response.status_code, 200)
		
#     def setUp(self):
# 		#입력데이터2 - 없는 아이디
#         self.data = {"username" : "test1", "password": "password"}
		

# 	def test_login(self):
# 		response = self.client.post(reverse('token_obtain_pair'), self.data)
# 		self.assertEqual(response.status_code, 200)
	
#     def setUp(self):
# 		#입력데이터1 - 옳은 데이터
# 		self.data = {"username" : "test", "password": "password"}
#         self.user = User.objects.create_user("test", "password")

# 	def test_login(self):
# 		response = self.client.post(reverse('token_obtain_pair'), self.data)
# 		self.assertEqual(response.status_code, 200)
		
#     def setUp(self):
# 		#입력데이터1 - 옳은 데이터
# 		self.data = {"username" : "test", "password": "password"}
#         self.user = User.objects.create_user("test", "password")

# 	def test_login(self):
# 		response = self.client.post(reverse('token_obtain_pair'), self.data)
# 		self.assertEqual(response.status_code, 200)
		