"""
URL configuration for YogaCollabHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from users.views import ProfileViewSet, TutorViewSet
from session.views import ClassTypeViewSet, YogaClassViewSet
from enrollment.views import EnrollmentViewSet
from interactions.views import YogahubViewSet, ChatRoomViewSet, ChatRoomMessageViewSet, MessageViewSet, NotificationViewSet


# Define a router for registering viewsets with default routes
router = routers.DefaultRouter()
router.register('Profiles', ProfileViewSet)
router.register('Tutors', TutorViewSet)
router.register('Class Types', ClassTypeViewSet)
router.register('Yoga Class', YogaClassViewSet)
router.register('Enrollment', EnrollmentViewSet)
router.register('Yoga Hub', YogahubViewSet)
router.register('Chat Room', ChatRoomViewSet)
router.register('Chat Room Message', ChatRoomMessageViewSet)
router.register('Message', MessageViewSet)
router.register('Notification', NotificationViewSet)


# Define urlpatterns for routing URLs to views
urlpatterns = [
    path('admin/', admin.site.urls),                        # Admin site URL
    path('', include('users.urls')),                        # Include URLs from the users app
    path('session/', include('session.urls')),              # Include URLs from the session app
    path('interactions/', include('interactions.urls')),    # Include URLs from the interactions app
    path('enrollment/', include('enrollment.urls')),        # Include URLs from the enrollment app
    path('aichatbot/', include('aichatbot.urls')),          # Include URLs from the aichatbot app
    path('api/', include(router.urls)),                     # Include API URLs registered with the router
] 
# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
