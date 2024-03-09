# I wrote this code
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification, Message, ChatRoom, ChatRoomMessage, Yogahub
from .forms import MessageForm, YogaHubForm, YogahubEditForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from users.serializers import YogahubSerializer, ChatRoomSerializer, ChatRoomMessageSerializer, MessageSerializer, NotificationSerializer

# View for the user's inbox
@login_required
def inbox(request):
    messages = request.user.received_messages.all()
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

# View for creating a new post
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

# View for displaying all yogahub posts
@login_required
def yogahub(request):
    logged_user = request.user
    status = Yogahub.objects.all()
    return render(request, 'interactions/yogahub.html', {'status': status, 'logged_user':logged_user})

# View for displaying the user's posts
@login_required
def mypost(request):
    loggedin_user = request.user
    mystatus = Yogahub.objects.filter(user=loggedin_user).first()
    return render(request, 'users/dashboard.html', {'mystatus': mystatus})

# View for displaying user notifications
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'interactions/notifications.html', {'notifications': notifications})

# View for displaying all chat rooms
@login_required
def chatrooms(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'interactions/chatrooms.html', {'chatrooms': chatrooms})

# View for displaying an individual chat room
@login_required
def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatRoomMessage.objects.filter(chatroom=chatroom)[0:30]
    return render(request, 'interactions/chatroom.html', {'chatroom': chatroom,'messages':messages})

# View for editing a Yogahub post
@login_required
def edit_yogahub(request, yogahub_id):
    edit_post= get_object_or_404(Yogahub, id=yogahub_id)
    if request.method == 'POST':
        editpostform = YogahubEditForm(request.POST, request.FILES, instance=yogahub_id)
        if editpostform.is_valid():
            editpostform.save()
            return redirect('dashboard_tutor')  # Redirect to dashboard after successful edit
    else:
        editpostform = YogahubEditForm(instance=request.user)
    return render(request, 'interactions/editpost.html', {'editpostform': editpostform, 'edit_post':edit_post})

# View for deleting a Yogahub post
@login_required
def delete_yogahub(request, yogahub_id):
    yogahub = get_object_or_404(Yogahub, pk=yogahub_id)
    yogahub.delete()
    return redirect('dashboard_tutor')


# ViewSet for Yogahub model
class YogahubViewSet(viewsets.ModelViewSet):
    queryset = Yogahub.objects.all()
    serializer_class = YogahubSerializer

# ViewSet for ChatRoom model
class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

# ViewSet for ChatRoomMessage model
class ChatRoomMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatRoomMessage.objects.all()
    serializer_class = ChatRoomMessageSerializer

# ViewSet for Message model
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# ViewSet for Notification model
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    


# end of code I wrote
