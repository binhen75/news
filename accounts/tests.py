from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model


# Create your tests here.
class TestCustomUser(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="super",
            email="super@example.com",
            password="testpass1234",
        )
        self.assertEqual(user.username, "super")
        self.assertEqual(user.email, "super@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_signup_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("templates/signup.html")
    
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("templates/signup.html")
    
    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
            "username": "testuser",
            "email": "testuser@email.com",
            "password1": "testpass123",
            "password2": "testpass123",
            },
            )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")


