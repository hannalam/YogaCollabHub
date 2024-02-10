from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('tutor_login/', views.tutor_login, name='tutor_login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done',auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='users/password_reset_form.html'),name='password_reset'),
    path('password_reset/done',auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done',auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('tutorRegister/', views.tutorRegister, name='tutorRegister'),
    path('edit/', views.edit, name='edit'),
    path('tutorEdit/', views.tutorEdit, name='tutorEdit'),
    path('profile/', views.profile, name='profile'),
    path('tutorProfile/', views.tutorProfile, name='tutorProfile'),
    path('invalid_credentials/', views.invalid, name='invalid'),
]