from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),  # Inbox for messages
    path('newpost/', views.new_post, name='new_post'), # Create a new post in yogahub
    path('yogahub/', views.yogahub, name='yogahub'),  # View for yogahub posts
    path('notifications/', views.notifications, name='notifications'),  # View for notifications
    path('chatrooms/', views.chatrooms, name='chatrooms'),  # View for chatrooms
    path('<slug:slug>/', views.chatroom, name='chatroom'),  # View for individual chatroom
    path('<int:yogahub_id>/delete/', views.delete_yogahub, name='delete_yogahub'),  # Delete yogahub post
    path('edit/<int:yogahub_id>/', views.edit_yogahub, name='edit_yogahub'),  # Edit yogahub post
] 
