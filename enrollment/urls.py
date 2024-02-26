from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('<int:class_id>/', views.enroll_class, name='enroll_class'),
    path('confirmation/', views.enroll_confirmation, name='enroll_confirmation'),
]
