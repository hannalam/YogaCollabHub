from django.urls import path

# I wrote this code

from .import consumers

# live chat websocket path setup
websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]


# end of code I wrote
