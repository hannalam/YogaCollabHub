from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    '''
    USER_TYPE_CHOICES = [
        ('student', 'Student User'),
        ('tutor', 'Tutor User'),
    ]
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    #user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
class Tutor(models.Model):
    #user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    teaching_certificate = models.FileField(upload_to='tutor/certificates/', blank=True, null=True)
    # Other fields specific to tutors

    def __str__(self):
        return self.user.username
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name