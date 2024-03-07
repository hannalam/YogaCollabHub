from django.db import models
from django.utils import timezone
from users.models import Profile, Tutor  
from django.conf import settings


# Model for the type of yoga class
class ClassType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Model for a yoga class session
class YogaClass(models.Model):
    title = models.CharField(max_length=100)
    class_type = models.ForeignKey(ClassType, on_delete=models.SET_NULL, null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    classroom_equipment = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    enrolled_students = models.ManyToManyField(Profile, related_name='enrolled_classes', blank=True)
    image_material = models.ImageField(upload_to='image_materials/', blank=True, null=True)  # Field for uploading images
    audio_material = models.FileField(upload_to='audio_materials/', blank=True, null=True) # Field for uploading audio files
    video_material = models.FileField(upload_to='video_materials/', blank=True, null=True) # Field for uploading video files


    def __str__(self):
        return f"{self.title} - {self.date} - {self.time}"
