from django.db import models
from users.models import Profile
from session.models import YogaClass

class Interaction(models.Model):
    yoga_class = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='liked_interactions')
    comment = models.TextField(blank=True, null=True)
    liked_by_user = models.ManyToManyField(Profile, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    interaction_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.user} - {self.yoga_class}"
    
