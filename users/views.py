from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Tutor
from .forms import UserEditForm, ProfileEditForm
from session.models import YogaClass

# user login request

def user_login(request):
    if request.method == "POST":           #if the request method is post, this will give the access to the login form
        form = LoginForm(request.POST)
        if form.is_valid():                #check if the input is clean data
            #data = form.cleaned_data
            #user = authenticate(request, username=data['username'], password=data['password'])

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)       #login to the specific user
                if 'is_tutor' in request.POST:
                    Tutor.objects.get_or_create(user_profile=user.profile)
                    # Redirect to tutor profile setup or dashboard
                    return HttpResponse("User authenticated as a tutor and logged in")
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse('Invalid credentials')
    
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

@login_required
def index(request):
    current_user = request.user
    #yoga_class = YogaClass.objects.filter(user=current_user)
    yoga_class = YogaClass.objects.all()
    return render(request,'users/index.html', {'yoga_class':yoga_class})

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

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_form':user_form, 'profile_form':profile_form})