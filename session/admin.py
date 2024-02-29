from django.contrib import admin
from .models import ClassType, YogaClass
# Register your models here.

#Custom Fields
class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_type', 'tutor', 'date', 'time', 'classroom_equipment', 'location', )

admin.site.register(ClassType)
admin.site.register(YogaClass, YogaClassAdmin)