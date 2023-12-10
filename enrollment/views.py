from django.shortcuts import render
from .models import Enrollment

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})

def enrollment_detail(request, enrollment_id):
    enrollment = Enrollment.objects.get(id=enrollment_id)
    return render(request, 'enrollment_detail.html', {'enrollment': enrollment})
# Other views for managing enrollments can be added here
