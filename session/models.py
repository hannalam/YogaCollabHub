from django.db import models
from django.utils import timezone
from users.models import Profile, Tutor  # Assuming a user profile model already exists
from django.conf import settings

class ClassType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

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


    def __str__(self):
        return f"{self.title} - {self.date} - {self.time}"
