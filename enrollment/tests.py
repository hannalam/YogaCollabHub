from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from enrollment.models import Enrollment
from enrollment.views import enroll_class


class EnrollmentViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create a test enrollment
        self.enrollment = Enrollment.objects.create(user=self.user)

    def test_enroll_session(self):
        # Log in as the test user
        self.client.login(username='testuser', password='password123')

        # Enroll the test user in a session (replace 'session_id' with actual session ID)
        response = self.client.post(reverse('enroll_class'))

        # Check if the enrollment was successful
        self.assertEqual(response.status_code, 302)  # Redirects to another page upon successful enrollment
        self.assertTrue(Enrollment.objects.filter(user=self.user).exists())