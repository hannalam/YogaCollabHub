from django import forms
from .models import Interaction

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ('yoga_class', 'student', 'interaction_type',)
