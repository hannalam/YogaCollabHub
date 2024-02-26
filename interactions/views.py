# I wrote this code
from django.shortcuts import render, redirect
from .models import Interaction, Notification, Message, ChatRoom, ChatRoomMessage
from .forms import InteractionForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def interaction_list(request):
    interactions = Interaction.objects.all()
    return render(request, 'interactions/interaction_list.html', {'interactions': interactions})

def add_interaction(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interaction_list')
    else:
        form = InteractionForm()
    return render(request, 'interactions/add_interaction.html', {'form': form})

def edit_interaction(request, interaction_id):
    interaction = Interaction.objects.get(pk=interaction_id)
    if request.method == 'POST':
        form = InteractionForm(request.POST, instance=interaction)
        if form.is_valid():
            form.save()
            return redirect('interaction_list')
    else:
        form = InteractionForm(instance=interaction)
    return render(request, 'interactions/edit_interaction.html', {'form': form, 'interaction': interaction})

def delete_interaction(request, interaction_id):
    interaction = Interaction.objects.get(pk=interaction_id)
    if request.method == 'POST':
        interaction.delete()
        return redirect('interaction_list')
    return render(request, 'interactions/delete_interaction.html', {'interaction': interaction})

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
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'interactions/notifications.html', {'notifications': notifications})

# Chat room main page
def chatrooms(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'interactions/chatrooms.html', {'chatrooms': chatrooms})

# Individual chat room page
def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatRoomMessage.objects.filter(chatroom=chatroom)[0:30]
    return render(request, 'interactions/chatroom.html', {'chatroom': chatroom,'messages':messages})
    #return render(request, 'interactions/chatroom.html', {'chatroom': chatroom})

# end of code I wrote
