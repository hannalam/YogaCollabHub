from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from aichatbot.views import aichatbot

class AIChatBotViewTestCase(TestCase):
    def setUp(self):
        # Create a test user (optional)
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_chatbot_view(self):
        # Create a mock request
        request = HttpRequest()
        request.user = self.user  # Attach the user to the request if authentication is required

        # Call the view function
        response = aichatbot(request)

        # Assert response status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aichatbot/chatbot.html')

    def test_chatbot_authenticated_view(self):
        # Create a mock request with an authenticated user
        request = HttpRequest()
        request.user = self.user

        # Call the view function
        response = aichatbot(request)

        # Assert that authenticated user can access the view
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aichatbot/chatbot.html')

