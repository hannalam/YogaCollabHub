from django import forms
from django.contrib.auth.models import User
from .models import Profile, Tutor

# Form for editing user details
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# Form for editing profile details
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio', 'location')


# Form for editing tutor user details
class TutorEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# Form for editing tutor profile details
class TutorProfileEditForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('profile_photo','bio', 'location')


# Form for editing tutor certification details
class TutorCertEditForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['teaching_certificate']  


# Login form for regular users
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Login form for tutors
class tutorLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Registration form for regular users
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


# Registration form for tutors
class TutorRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name'}

    def check_password(self):
        if self.cleaned_data['password']!= self.cleaned_data['password2']:
            raise forms.ValidationError('Password do not match')
        return self.cleaned_data['password2']