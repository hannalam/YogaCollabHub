from django import forms
from .models import YogaClass

class SessionForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ('title', 'class_type', 'tutor', 'date','time', 'classroom_equipment', 'description', 'location')

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ['enrolled_students']