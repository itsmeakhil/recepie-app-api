from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        email = "akhil@gmail.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
