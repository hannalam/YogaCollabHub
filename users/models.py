from django.db import models
from django.conf import settings

# Profile model to store user profiles
class Profile(models.Model):
    '''   
    #This was the option I had when designing the users
    USER_TYPE_CHOICES = [
        ('student', 'Student User'),
        ('tutor', 'Tutor User'),
    ]
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

# Tutor model to represent users who are tutors
class Tutor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    teaching_certificate = models.FileField(upload_to='tutor/certificates/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name