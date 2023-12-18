from django.shortcuts import render, redirect, get_object_or_404
from .models import YogaClass, ClassType
from users.models import Profile
from interactions.models import Interaction
from .forms import SessionForm, EnrollmentForm
from django.contrib.auth.decorators import login_required

def class_list(request):
    classes = YogaClass.objects.all()
    class_tutor = Profile.objects.all()
    class_interaction = Interaction.objects.all()
    return render(request, 'session/class_list.html', {'classes': classes, 'class_tutor':class_tutor, 'class_interaction':class_interaction})

def class_detail(request, class_id):
    yoga_class = YogaClass.objects.get(id=class_id)
    return render(request, 'session/class_detail.html', {'yoga_class': yoga_class})

def add_class_type(request):
    if request.method == 'POST':
        new_type = request.POST.get('new_type')
        ClassType.objects.create(name=new_type)
        # Handle form submission or redirect as needed
    return render(request, 'session/add_class_type.html')
# Other views for managing classes, enrollment, scheduling, etc., can be added here

@login_required
def create_class(request):
    if request.method == 'POST':
        form = SessionForm(data=request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.tutor = request.user.profile  # Assuming user profile is linked
            new_class.save()
            return redirect('class_list')
    else:
        form = SessionForm()
    return render(request, 'session/create_class.html', {'form': form})

def enroll_class(request, class_id):
    enroll_class = get_object_or_404(YogaClass, id=class_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            # Add the student to the enrolled_students field
            student_profile = request.user.profile  # Assuming user profile is linked
            enroll_class.enrolled_students.add(student_profile)
            return redirect('class_detail', class_id=class_id)
    else:
        form = EnrollmentForm()
    return render(request, 'session/enroll_class.html', {'form': form, 'enroll_class': enroll_class})

def schedule_class(request, class_id):
    schedule_class = get_object_or_404(YogaClass, id=class_id)
    # Logic for scheduling the class
    return render(request, 'session/schedule_class.html', {'schedule_class': schedule_class})

def dashboard(request):
    dashboard = YogaClass.objects.all()
    return render(request, 'session/dashboard.html', {'dashboard':dashboard})