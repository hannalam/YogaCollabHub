from django import forms
from .models import Interaction, Message, Yogahub

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ('yoga_class', 'user', 'comment',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']

class YogaHubForm(forms.ModelForm):
    class Meta:
        model = Yogahub
        fields = ('title', 'image', 'caption')