from django import forms
from django.contrib.auth.models import User
from .models import Profile, Tutor


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio', 'location')

class TutorEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class TutorProfileEditForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('profile_photo','bio', 'location')

class TutorCertEditForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['teaching_certificate']  

# login form

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# tutor login form

class tutorLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Registration Form
    
class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name'}

    def check_password(self):
        if self.cleaned_data['password']!= self.cleaned_data['password2']:
            raise forms.ValidationError('Password do not match')
        return self.cleaned_data['password2']
    
class TutorRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    #user_type = forms.ChoiceField(choices=[('student', 'Student'), ('tutor', 'Tutor')], widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name'}

    def check_password(self):
        if self.cleaned_data['password']!= self.cleaned_data['password2']:
            raise forms.ValidationError('Password do not match')
        return self.cleaned_data['password2']