from unittest.mock import patch
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User

USER_REGISTER_URL = reverse("accounts:register")
TEST_USER_DATA = {
    "username": "test_username",
    "email": "test@gmail.com",
    "first_name": "First",
    "last_name": "Last",
    "password": "!H@3ajXQzvD68D%2EiN!",
    "confirm_password": "!H@3ajXQzvD68D%2EiN!"
}


class UserRegisterTests(APITestCase):
    def test_user_register(self):
        users_before = User.objects.all().count()

        request = self.client.post(USER_REGISTER_URL, TEST_USER_DATA)

        users_after = User.objects.all().count()

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(users_after - users_before, 1)
        self.assertTrue(User.objects.filter(username="test_username").exists())

    def test_wrong_password_confirm(self):
        TEST_USER_DATA["confirm_password"] = "sdfgdbaerawe"
        request = self.client.post(USER_REGISTER_URL, TEST_USER_DATA)

        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            request.data,
            {"password": ["Password fields didn't match."]}
        )
        self.assertFalse(User.objects.filter(username="test_username").exists())
