from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('session', 'material_type', 'content',)  # Adjust fields as needed
