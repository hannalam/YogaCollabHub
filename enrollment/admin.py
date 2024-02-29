from django.contrib import admin
from .models import Enrollment

#Custom Fields
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'enrollment_date')


admin.site.register(Enrollment, EnrollmentAdmin)