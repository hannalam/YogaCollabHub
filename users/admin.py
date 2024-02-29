from django.contrib import admin
from .models import Profile, Tutor

# Register your models here.

admin.site.register(Profile)
admin.site.register(Tutor)

#Update Custom Headers
admin.site.site_header = "Yoga Collab Hub Site"
admin.site.site_title = "Yoga Collab Hub"
admin.site.index_title = "Manage Yoga Collab Hub"