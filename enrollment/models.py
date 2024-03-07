from django.db import models
from users.models import Profile   # Import the Profile model from the 'users' app
from session.models import YogaClass   # Import the YogaClass model from the 'session' app

class Enrollment(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)   # ForeignKey relationship with the Profile model
    session = models.ForeignKey(YogaClass, on_delete=models.CASCADE)   # ForeignKey relationship with the YogaClass model
    enrollment_date = models.DateTimeField(auto_now_add=True)   # DateTimeField to store the enrollment date
    confirmed = models.BooleanField(default=False)   # BooleanField to indicate if enrollment is confirmed or not

    def __str__(self):
        return f"{self.student} - {self.session}"
