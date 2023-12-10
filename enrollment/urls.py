from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('<int:enrollment_id>/', views.enrollment_detail, name='enrollment_detail'),
    # Define other URL patterns for enrollment-related views
]
