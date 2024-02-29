from django.test import TestCase
from users.model_factories import ProfileFactory
from users.models import Profile 

class ProfileTestCase(TestCase):
    def test_create_profile(self):
        profile = ProfileFactory()
        # Now you can use 'profile' object in your test case

    # Verify that the profile was created successfully
        self.assertIsNotNone(profile)  # Check if profile object exists
        self.assertIsInstance(profile, Profile)  # Check if profile is an instance of Profile model
        self.assertTrue(Profile.objects.exists())  # Check if profile exists in the database