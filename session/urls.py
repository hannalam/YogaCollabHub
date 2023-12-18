from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('create/', views.create_class, name='create_class'),
    path('<int:class_id>/', views.class_detail, name='class_detail'),
    path('add_class_type/', views.add_class_type, name='add_class_type'),
    path('dashboard/', views.dashboard, name='dashboard'),

]

