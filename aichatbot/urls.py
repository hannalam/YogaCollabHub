from django.urls import path
from . import views

urlpatterns = [
    path('', views.aichatbot, name='aichatbot'),  # Endpoint for accessing the AI chatbot
    path('new_chat/', views.new_chat, name='new_chat'),  # Endpoint for starting a new chat session
    path('error-handler/', views.error_handler, name='error_handler'),  # Endpoint for error handling
]
