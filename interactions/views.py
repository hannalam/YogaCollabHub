# I wrote this code
from django.shortcuts import render, redirect
from .models import Notification, Message, ChatRoom, ChatRoomMessage, Yogahub
from .forms import MessageForm, YogaHubForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from users.serializers import YogahubSerializer, ChatRoomSerializer, ChatRoomMessageSerializer, MessageSerializer, NotificationSerializer

@login_required
def inbox(request):
    messages = request.user.received_messages.all()
    #messages = Message.objects.filter(recipient=request.user)
    if request.method == 'POST':
        mes_form = MessageForm(request.POST)
        if mes_form.is_valid():
            message = mes_form.save(commit=False)
            message.sender = request.user
            message.save()
            Notification.objects.create(user=message.receiver, message="You have a new message.")
            return redirect('inbox')
    else:
        mes_form = MessageForm()
    return render(request, 'interactions/inbox.html', {'messages': messages, 'mes_form': mes_form})

@login_required
def new_post(request):
    if request.method == 'POST':
        yogahubform = YogaHubForm(data=request.POST, files=request.FILES)
        if yogahubform.is_valid():
            new_post = yogahubform.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('yogahub')

    else:
        yogahubform = YogaHubForm(data=request.GET)
    return render(request, 'interactions/newpost.html', {'yogahubform': yogahubform})

@login_required
def yogahub(request):
    logged_user = request.user
    status = Yogahub.objects.all()
    return render(request, 'interactions/yogahub.html', {'status': status, 'logged_user':logged_user})

@login_required
def mypost(request):
    loggedin_user = request.user
    mystatus = Yogahub.objects.filter(user=loggedin_user).first()
    #profile = Profile.objects.filter(user=loggedin_user).first()
    return render(request, 'users/dashboard.html', {'mystatus': mystatus})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'interactions/notifications.html', {'notifications': notifications})

@login_required
# Chat room main page
def chatrooms(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'interactions/chatrooms.html', {'chatrooms': chatrooms})

@login_required
# Individual chat room page
def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatRoomMessage.objects.filter(chatroom=chatroom)[0:30]
    return render(request, 'interactions/chatroom.html', {'chatroom': chatroom,'messages':messages})
    #return render(request, 'interactions/chatroom.html', {'chatroom': chatroom})

class YogahubViewSet(viewsets.ModelViewSet):
    queryset = Yogahub.objects.all()
    serializer_class = YogahubSerializer

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class ChatRoomMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatRoomMessage.objects.all()
    serializer_class = ChatRoomMessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    


# end of code I wrote
