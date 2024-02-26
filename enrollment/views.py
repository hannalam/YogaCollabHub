from django.shortcuts import render, redirect,get_object_or_404
from .models import Enrollment
from session.models import YogaClass 
from .forms import EnrollmentForm
from django.contrib.auth.decorators import login_required

@login_required
def enroll_confirmation(request, class_id):
    yoga_class = get_object_or_404(YogaClass, pk=class_id)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user.profile, session=yoga_class)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        enroll_forms = EnrollmentForm(request.POST)

        # Check if the form is valid
        if enroll_forms.is_valid():
            # Update the confirmed status based on form input
            enrollment.confirmed = True
            enrollment.save()

            # Redirect to the dashboard upon successful enrollment confirmation
            return redirect('dashboard')  # Replace 'dashboard' with the actual URL name for your dashboard page

    else:
        # If a GET (or any other method) we'll create a blank form
        enroll_forms = EnrollmentForm()
    return render(request, 'enrollment/enroll_confirmation.html', {'enrollment': enrollment, 'enroll_forms':enroll_forms})


@login_required
def enroll_class(request, class_id):
    yoga_class = get_object_or_404(YogaClass, pk=class_id)

    # Create a new enrollment
    enroll = Enrollment.objects.create(student=request.user.profile, session=yoga_class)
    
    # Check if the user is already enrolled in the class
    #enrollment, created = Enrollment.objects.get_or_create(student=request.user.profile, session=yoga_class)
    #if not created and enrollment.confirmed:
        # If already enrolled and confirmed, redirect with a message indicating that
        #messages.info(request, 'You are already enrolled in this class.')
    
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        enroll_form = EnrollmentForm(request.POST)

        # Check if the form is valid
        if enroll_form.is_valid():
            # Update the confirmed status based on form input
            #enroll.confirmed = True
            enroll.save()

            # Redirect to the dashboard upon successful enrollment confirmation
            return redirect('dashboard')  # Replace 'dashboard' with the actual URL name for your dashboard page

    else:
        # If a GET (or any other method) we'll create a blank form
        enroll_form = EnrollmentForm()
    return render(request, 'enrollment/enroll_confirmation.html', {'enroll': enroll, 'enroll_form':enroll_form})

    # If not already enrolled or not confirmed, create a new enrollment
    # and redirect to the confirmation page
    #return redirect('enroll_confirmation', enrollment_id=enrollment.id)

