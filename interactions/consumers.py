# I wrote this code

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, ChatRoomMessage


class ChatConsumer(AsyncWebsocketConsumer):

    # the chat room name and users will be connected
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # no connection and just wait the next connection
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.channel_layer,
            self.room_group_name
        )

    # when the message is recevied, assign the input to the right places
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
            }
        )

        await self.save_message(username, room, message)

    # store and transfer messages into a file in the form of JSONs
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
        }))


    # save the chat messages to the database
    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)
        ChatRoomMessage.objects.create(
            user=user, chatroom=room, messages=message)


# end of code I wrote
