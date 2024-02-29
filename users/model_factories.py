import factory
from django.contrib.auth.models import User
from django.core.files import File

from .models import *

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')

class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    profile_photo = factory.django.ImageField(width=100, height=100)
    bio = factory.Faker('paragraph')
    location = factory.Faker('city')
    tutor = None 