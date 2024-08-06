from django.test import TestCase
from .models import CustomUser
from django.contrib.auth.models import User


# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        user = User.objects.create(username="testuser", password="testpassword")
        CustomUser.objects.create(user=user, name="test", bio="Hey!")

    def test_user_name(self):
        """Test to ensure that user's name is initialized correctly"""
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_user_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field("name").max_length
        self.assertEqual(max_length, 120)

    def test_users_pic(self):
        """test to see if the default image is used if no other pic uploaded"""
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.picture, "no_picture.jpg")

    def test_user_username_max_length(self):
        """test to check if the length of the username field is a maximum of 120 characters"""
        user = CustomUser.objects.get(id=1)
        max_length = user.user._meta.get_field("username").max_length
        self.assertEqual(max_length, 150, "username has over 120 characters")

    def test_user_bio(self):
        """test to check if the user's bio is initialized as expected"""
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field("bio").verbose_name
        self.assertEqual(field_label, "bio")
