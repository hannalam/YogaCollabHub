from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, TutorRegistrationForm, tutorLoginForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Tutor
from .forms import UserEditForm, ProfileEditForm, TutorEditForm, TutorProfileEditForm, TutorCertEditForm

# user login request

def user_login(request):
    if request.method == "POST":           #if the request method is post, this will give the access to the login form
        form = LoginForm(request.POST)
        if form.is_valid():                #check if the input is clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)       #login to the specific user
                return redirect('profile')
            else:
                return render(request, 'users/invalid_credentials.html')  
    
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

def tutor_login(request):
    if request.method == "POST":           #if the request method is post, this will give the access to the login form
        tutor_form = tutorLoginForm(request.POST)
        if tutor_form.is_valid():                #check if the input is clean data
            username = tutor_form.cleaned_data['username']
            password = tutor_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)       #login to the specific user
                return redirect('tutorProfile')
            else:
                return render(request, 'users/invalid_credentials.html')  
    else:
        tutor_form = tutorLoginForm()
    return render(request, 'users/tutor_login.html', {'tutor_form':tutor_form})

def index(request):
    return render(request,'users/index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:   
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form':user_form})

def tutorRegister(request):
    if request.method == 'POST':
        tutor_form = TutorRegistrationForm(request.POST, request.FILES)
        if tutor_form.is_valid():
            new_user = tutor_form.save(commit=False)
            new_user.set_password(tutor_form.cleaned_data['password'])
            new_user.save()
            Tutor.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:   
        tutor_form = TutorRegistrationForm()
    return render(request, 'users/tutorRegister.html', {'tutor_form':tutor_form})

@login_required
def edit(request):
    loggedin_user = request.user
    edit_profile = Profile.objects.filter(user=loggedin_user)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_form':user_form, 'profile_form':profile_form, 'edit_profile':edit_profile})

@login_required
def tutorEdit(request):
    loggedin_user = request.user
    tutor_edit_profile = Tutor.objects.filter(user=loggedin_user) 
    cert_form = Tutor.objects.filter(user=loggedin_user) 
    if request.method == 'POST':
        tutor_user_form = TutorEditForm(instance=request.user, data=request.POST)
        tutor_profile_form = TutorProfileEditForm(instance=request.user, data=request.POST, files=request.FILES)
        cert_form = TutorCertEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if tutor_user_form.is_valid() and cert_form.is_valid() and tutor_profile_form.is_valid():
            tutor_user_form.save()
            tutor_profile_form.save()
            cert_form.save()
            return redirect('tutorProfile')
    else:
        tutor_user_form = TutorEditForm(instance=request.user)
        tutor_profile_form = TutorProfileEditForm(instance=request.user)
        cert_form = TutorCertEditForm(instance=request.user)
    return render(request, 'users/tutorEdit.html', {'tutor_user_form':tutor_user_form, 'tutor_profile_form':tutor_profile_form, 'tutor_edit_profile':tutor_edit_profile, 'cert_form':cert_form})

@login_required
def profile(request):
    loggedin_user = request.user
    profile = Profile.objects.filter(user=loggedin_user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def tutorProfile(request):
    loggedin_user = request.user
    tutorProfile = Tutor.objects.filter(user=loggedin_user)
    tutorCert = Tutor.objects.filter(user=loggedin_user)
    return render(request, 'users/tutorProfile.html', {'tutorProfile': tutorProfile, 'tutorCert':tutorCert})


def invalid(request):
    return render(request, 'users/invalid_credentials.html')

@login_required
def settings(request):
    loggedin_user = request.user
    profile_setting = Profile.objects.filter(user=loggedin_user)
    return render(request, 'users/settings.html', {'profile_setting': profile_setting})

@login_required
def setting(request):
    loggedin_user = request.user
    tutor_setting = Tutor.objects.filter(user=loggedin_user)
    return render(request, 'users/setting.html', {'tutor_setting': tutor_setting})