from django.db import models
from session.models import YogaClass  # Assuming a YogaClass model already exists
from users.models import Profile, Tutor
from django.utils import timezone

def material_upload_path(instance, filename):
    # Constructing the upload path dynamically based on current timestamp
    return f"materials/{instance.material_type}/{timezone.now().strftime('%Y/%m/%d')}/{filename}"

class Material(models.Model):
    session = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    UPLOAD_TYPES = [
        ('Video', 'Video'),
        ('Photo', 'Photo'),
        ('Text', 'Text'),
        ('Audio', 'Audio'),
    ]
    material_type = models.CharField(max_length=50, choices=UPLOAD_TYPES)
    content = models.TextField()
    uploaded_by = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    upload_datetime = models.DateTimeField(auto_now_add=True)
    material_file = models.FileField(upload_to=material_upload_path)

    def __str__(self):
        return f"{self.material_type} - {self.session}"
