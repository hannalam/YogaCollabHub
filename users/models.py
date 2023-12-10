from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Tutor(models.Model):
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    teaching_certificate = models.FileField(upload_to='tutor/certificates/', blank=True, null=True)
    # Other fields specific to tutors

    def __str__(self):
        return self.user_profile.user.username