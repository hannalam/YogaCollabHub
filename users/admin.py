from django.contrib import admin
from .models import Profile, Tutor

# Define custom admin configurations for the Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo','bio', 'location')

# Define custom admin configurations for the Tutor model
class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_photo','bio', 'location')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tutor, TutorAdmin)

#Update Custom Headers
admin.site.site_header = "Yoga Collab Hub Site"
admin.site.site_title = "Yoga Collab Hub"
admin.site.index_title = "Manage Yoga Collab Hub"

