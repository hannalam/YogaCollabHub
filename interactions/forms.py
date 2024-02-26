from django import forms
from .models import Interaction, Message

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ('yoga_class', 'user', 'comment',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']