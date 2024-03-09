from django import forms
from .models import Enrollment

# Form for Enrollment
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ('confirmed',) 
