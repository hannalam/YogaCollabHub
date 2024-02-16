from django import forms
from .models import YogaClass
from interactions.models import Comment

class SessionForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ('title', 'class_type', 'tutor', 'date','time', 'classroom_equipment', 'description', 'location')

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ['enrolled_students']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','posted_by',)

class ClassEditForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ('title', 'class_type', 'tutor', 'date','time', 'classroom_equipment', 'description', 'location')