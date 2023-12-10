from django.db import models
from users.models import Profile  # Assuming a user profile model already exists
from session.models import YogaClass  # Assuming a Session model already exists

class Enrollment(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    session = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  # Pending, Approved, Rejected

    def __str__(self):
        return f"{self.student} - {self.session}"
