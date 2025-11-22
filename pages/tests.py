from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class StaticPagesTest(SimpleTestCase):
    def test_response_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_response_home_reverse(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")

