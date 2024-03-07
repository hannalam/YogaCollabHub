from django import forms
from .models import Interaction, Message, Yogahub

# Form for creating or editing an Interaction
class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ('yoga_class', 'user', 'comment',)

# Form for sending a message
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']

# Form for creating or editing a Yogahub entry
class YogaHubForm(forms.ModelForm):
    class Meta:
        model = Yogahub
        fields = ('title', 'image', 'caption')

# Form for editing an existing Yogahub entry
class YogahubEditForm(forms.ModelForm):
    class Meta:
        model = Yogahub
        fields = ('title', 'image', 'caption')