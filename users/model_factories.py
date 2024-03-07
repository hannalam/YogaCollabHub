import factory
from django.contrib.auth.models import User
from django.core.files import File
from .models import *

# Factory class for generating User instances
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')     # Generate a fake username
    email = factory.Faker('email')            # Generate a fake email
 

# Factory class for generating Profile instances
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)     # Create a User instance associated with the Profile using the UserFactory
    profile_photo = factory.django.ImageField(width=100, height=100)   # Generate a fake profile photo
    bio = factory.Faker('paragraph')           # Generate a fake bio
    location = factory.Faker('city')           # Generate a fake location (city)
    tutor = None 