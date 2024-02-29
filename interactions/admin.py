from django.contrib import admin
from .models import Interaction, Comment, Message, Notification, ChatRoom, ChatRoomMessage, Yogahub

#Custom Fields
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class ChatRoomMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'chatroom', 'messages', 'date')

class YogahubAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'title', 'caption', 'date')

admin.site.register(Interaction)
admin.site.register(Comment)
admin.site.register(Message, MessageAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(ChatRoomMessage, ChatRoomMessageAdmin)
admin.site.register(Yogahub, YogahubAdmin)
