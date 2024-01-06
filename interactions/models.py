from django.db import models
from django.conf import settings
from users.models import Profile
from session.models import YogaClass

class Interaction(models.Model):
    yoga_class = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='liked_interactions')
    comment = models.TextField(blank=True, null=True)
    liked_by_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='session_like', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    interaction_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.user} - {self.yoga_class}"
    
class Comment(models.Model):
    session_comment = models.ForeignKey(Interaction, on_delete=models.CASCADE, related_name='session_comment')
    body = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.body