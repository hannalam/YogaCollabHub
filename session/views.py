from django.shortcuts import render, redirect, get_object_or_404
from .models import YogaClass, ClassType
from enrollment.models import Enrollment
from users.models import Profile, Tutor
from interactions.models import Interaction, Yogahub
from .forms import SessionForm, EnrollmentForm, CommentForm, ClassEditForm, ClassTypeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from users.serializers import ClassTypeSerializer, YogaClassSerializer


# View for adding a new class type
def add_class_type(request):
    if request.method == 'POST':
        type_form = ClassTypeForm(data=request.POST)
        if type_form.is_valid():
            type_form.save()
            return redirect('create_class')
    else:
        type_form = ClassTypeForm()
    return render(request, 'session/class_type.html', {'type_form':type_form})


# View for creating a new class
@login_required
def create_class(request):
    types = ClassType.objects.all()
    if request.method == 'POST':
        form = SessionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.tutor = request.user.profile  
            new_class.save()
            return redirect('dashboard_tutor')
    else:
        form = SessionForm()
    return render(request, 'session/create_class.html', {'form': form, 'types':types})


# Views for displaying the list of classes
@login_required
def class_list(request):
    classes = YogaClass.objects.all()   # Retrieve all yoga classes

    class_name = request.GET.get('class_name')          # Search functionality
    if class_name != '' and class_name is not None:
        classes = classes.filter(title__icontains=class_name)

    paginator = Paginator(classes,5)    # Pagination
    page = request.GET.get('page')
    classes = paginator.get_page(page)

    logged_user = request.user     # Get logged-in user
    return render(request, 'session/class_list.html', {'classes': classes, 'logged_user':logged_user})


# Views for displaying the list of classes for tutors
@login_required
def class_list_tutor(request):
    # Retrieve all yoga classes
    classes_t = YogaClass.objects.all()
    class_tutor_t = Tutor.objects.all()
    class_interaction_t = Interaction.objects.all()
    logged_user = request.user
    return render(request, 'session/class_list_tutor.html', {'classes_t': classes_t, 'class_tutor_t':class_tutor_t, 'class_interaction_t':class_interaction_t, 'logged_user':logged_user})


# View for displaying details of a class
@login_required
def class_detail(request, class_id):
    # Retrieve the yoga class object
    yoga_class = get_object_or_404(YogaClass, id=class_id)
    interaction_t = Interaction.objects.filter(yoga_class=yoga_class)
    comment_form_t = CommentForm(data=request.POST)
    if request.method == 'POST':        # Handle POST request for adding comments
        if comment_form_t.is_valid():
            new_comment = comment_form_t.save(commit=False)
            session_id = request.POST.get('session_id')
            session = get_object_or_404(Interaction, id=session_id)
            new_comment.post = session
            new_comment.save()
        else:
            comment_form_t = CommentForm()

    logged_user = request.user
    return render(request, 'session/class_detail.html', {'yoga_class': yoga_class, 'interaction_t':interaction_t, 'comment_form_t': comment_form_t,'logged_user':logged_user})


# View for displaying class details to students
@login_required
def class_detail_student(request, class_id):
    yoga_class_detail = get_object_or_404(YogaClass, pk=class_id)     # Retrieve the yoga class object
    interactions = Interaction.objects.filter(yoga_class=yoga_class_detail)         # Retrieve interactions related to the specified yoga class

    # Handle POST request for adding comments
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            session_id = request.POST.get('session_id')
            session = get_object_or_404(Interaction, id=session_id)
            new_comment.post = session
            new_comment.save()
    else:
        comment_form = CommentForm()

    logged_user = request.user
    return render(request, 'session/class_detail_student.html', {'yoga_class_detail': yoga_class_detail, 'interactions':interactions, 'comment_form': comment_form,'logged_user':logged_user})


# View for editing a class
@login_required
def edit_class(request):
    loggedin_user = request.user
    edit_class = Profile.objects.filter(user=loggedin_user)
    if request.method == 'POST':
        edit_form = ClassEditForm(instance=request.user, data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard_tutor')
    else:
        edit_form = ClassEditForm(instance=request.user)

    return render(request, 'session/edit_class.html', {'edit_form':edit_form, 'edit_class':edit_class})


# View for deleting a class
@login_required
def delete_class(request, class_id):
    if request.method == 'POST':
        yoga_class = YogaClass.objects.get(id=class_id)
        yoga_class.delete()
        return redirect('class_list_tutor')
    else:
        return render(request, 'session/class_delete_confirm.html', {'class_id': class_id})


# View for enrolling in a class
@login_required
def enroll_class(request, class_id):
    enroll_class = get_object_or_404(YogaClass, id=class_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student_profile = request.user.profile  
            enroll_class.enrolled_students.add(student_profile)
            return redirect('class_detail', class_id=class_id)
    else:
        form = EnrollmentForm()
    return render(request, 'session/enroll_class.html', {'form': form, 'enroll_class': enroll_class})


# View for deleting enrolled class
@login_required
def delete_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('dashboard')
    return redirect('class_list')


# View for dashboard
@login_required
def dashboard(request):
    enrolled_classes = Enrollment.objects.filter(student=request.user.profile)
    loggedin_user = request.user
    mystatus = Yogahub.objects.filter(user=loggedin_user)
    return render(request, 'session/dashboard.html', {'enrolled_classes':enrolled_classes,'mystatus': mystatus})


# View for tutor dashboard
@login_required
def dashboard_tutor(request):
    class_type = ClassType.objects.all()
    dashboard_t = YogaClass.objects.all()
    logged_user = request.user
    tutorstatus = Yogahub.objects.filter(user=logged_user)
    return render(request, 'session/dashboard_tutor.html', {'dashboard_t':dashboard_t, 'logged_user':logged_user, 'class_type':class_type, 'tutorstatus':tutorstatus})


# Views for like/unlike action
@login_required
def session_like(request):
    session_id = request.POST.get('session_id')
    session = get_object_or_404(Interaction, id=session_id )
    if session.liked_by_user.filter(id=request.user.id).exists():
        session.liked_by_user.remove(request.user)
    else:
        session.liked_by_user.add(request.user)
    return redirect('dashboard')


# ViewSets for ClassType and YogaClass models
class ClassTypeViewSet(viewsets.ModelViewSet):
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeSerializer

class YogaClassViewSet(viewsets.ModelViewSet):
    queryset = YogaClass.objects.all()
    serializer_class = YogaClassSerializer