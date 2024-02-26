from django.contrib import admin
from .models import Interaction, Comment, Message, Notification, ChatRoom, ChatRoomMessage

admin.site.register(Interaction)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(ChatRoom)
admin.site.register(ChatRoomMessage)