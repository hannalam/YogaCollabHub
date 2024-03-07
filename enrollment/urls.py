from django.urls import path
from . import views

urlpatterns = [
    path('<int:class_id>/', views.enroll_class, name='enroll_class'),   # Path to enroll in a specific class, identified by class_id
    path('confirmation/', views.enroll_confirmation, name='enroll_confirmation'),   # Path to handle enrollment confirmation
]
