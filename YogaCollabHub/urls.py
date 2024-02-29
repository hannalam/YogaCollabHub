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



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('session/', include('session.urls')),
    path('interactions/', include('interactions.urls')),
    path('enrollment/', include('enrollment.urls')),
    path('aichatbot/', include('aichatbot.urls')),
    path('api/', include(router.urls)),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
