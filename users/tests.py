from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile, Tutor
from .forms import UserRegistrationForm, TutorRegistrationForm, UserEditForm, TutorEditForm
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import ProfileSerializer, TutorSerializer

#Test user authentication:
class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Assert redirect on successful login

    def test_invalid_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)  # Assert login page reloads on invalid login

#Test tutor registration:
class TutorRegistrationTestCase(TestCase):
    def test_tutor_registration_valid_data(self):
        form_data = {'username': 'tutoruser', 'email': 'tutor@example.com', 'password': 'tutorpass', 'password2': 'tutorpass'}
        form = TutorRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tutor_registration_invalid_data(self):
        form_data = {'username': '', 'email': 'invalid_email', 'password': 'pass', 'password2': 'pass_mismatch'}
        form = TutorRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

#Test profile editing:
class ProfileEditingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.profile = Profile.objects.create(user=self.user)

    def test_editing_user_profile_valid_data(self):
        form_data = {'first_name': 'Test', 'last_name': 'User', 'email': 'test@example.com'}
        form = UserEditForm(instance=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_editing_user_profile_invalid_data(self):
        form_data = {'first_name': '', 'last_name': '', 'email': ''}
        form = UserEditForm(instance=self.user, data=form_data)
        self.assertFalse(form.is_valid())

    def test_editing_tutor_profile_valid_data(self):
        form_data = {'first_name': 'Test', 'last_name': 'Tutor', 'email': 'tutor@example.com'}
        form = TutorEditForm(instance=self.tutor, data=form_data)
        self.assertTrue(form.is_valid())

    def test_editing_tutor_profile_invalid_data(self):
        form_data = {'first_name': '', 'last_name': '', 'email': ''}
        form = TutorEditForm(instance=self.tutor, data=form_data)
        self.assertFalse(form.is_valid())

#Test viewsets
class ProfileViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.client = Client()

    def test_profile_view_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_anonymous_user(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirects to login


class TutorProfileViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testtutor', email='tutor@example.com')
        self.tutor = Tutor.objects.create(user=self.user)
        self.client = Client()

    def test_tutor_profile_view_authenticated_tutor(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tutorProfile'))
        self.assertEqual(response.status_code, 200)

    def test_tutor_profile_view_anonymous_user(self):
        response = self.client.get(reverse('tutorProfile'))
        self.assertEqual(response.status_code, 302)  # Redirects to login

class SettingsViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.profile = Profile.objects.create(user=self.user)
        self.tutor = Tutor.objects.create(user=self.user)
        self.client = Client()

    def test_settings_view_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)

    def test_settings_view_authenticated_tutor(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('setting'))
        self.assertEqual(response.status_code, 200)

class InvalidCredentialsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_invalid_credentials_view_rendering(self):
        response = self.client.get(reverse('invalid'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/invalid_credentials.html')

class ProfileViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.profile = Profile.objects.create(user=self.user)
        self.tutor = Tutor.objects.create(user=self.user)

    def test_profile_viewset(self):
        url = reverse('profile-list')
        response = self.client.get(url)
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tutor_viewset(self):
        url = reverse('tutor-list')
        response = self.client.get(url)
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)