from django.contrib import admin
from .models import Profile, Tutor

# Register your models here.

#Custom Fields
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo','bio', 'location')

class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo','bio', 'location')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tutor, TutorAdmin)

#Update Custom Headers
admin.site.site_header = "Yoga Collab Hub Site"
admin.site.site_title = "Yoga Collab Hub"
admin.site.index_title = "Manage Yoga Collab Hub"

