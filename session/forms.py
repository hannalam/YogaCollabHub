from django import forms
from .models import YogaClass, ClassType
from interactions.models import Comment

# Form for creating or editing a YogaClass session
class SessionForm(forms.ModelForm):

    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model = YogaClass
        fields = ('title', 'class_type', 'tutor', 'date','time', 'classroom_equipment', 'description', 'location','image_material', 'audio_material', 'video_material',)

# Form for enrolling students in a YogaClass session
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ['enrolled_students']

# Form for adding comments to a YogaClass session
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','posted_by',)

# Form for editing a YogaClass session
class ClassEditForm(forms.ModelForm):
    class Meta:
        model = YogaClass
        fields = ('title', 'class_type', 'tutor', 'date','time', 'classroom_equipment', 'description', 'location','image_material', 'audio_material', 'video_material',)
        
    class DateForm(forms.Form):
        date = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        )

# Form for adding or editing a ClassType
class ClassTypeForm(forms.ModelForm):
    class Meta:
        model = ClassType
        fields = ('name',)