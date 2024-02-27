from django.db import models
from django.conf import settings
from users.models import Profile
from session.models import YogaClass
from django.contrib.auth.models import User
from django.utils.text import slugify

# I wrote this code

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
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


# model for chatroom setup
class ChatRoom(models.Model):

    # show the chatroom name in the admin page
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

# model for chatroom message setup
class ChatRoomMessage(models.Model):

    # show the messages in the admin page
    def __str__(self):
        return self.messages

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    messages = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

class Yogahub(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%M/%D')
    title = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    #slug = models.SlugField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='likecount', blank=True)

    # show the status title in the admin page
    def __str__(self):
        return self.title

    # save the slug
    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = slugify(self.title)
        #super().save(*args, **kwargs)

# end of code I wrote
