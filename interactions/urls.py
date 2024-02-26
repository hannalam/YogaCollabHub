from django.urls import path
from . import views

urlpatterns = [
    path('', views.interaction_list, name='interaction_list'),
    path('add/', views.add_interaction, name='add_interaction'),
    path('edit/<int:interaction_id>/', views.edit_interaction, name='edit_interaction'),
    path('delete/<int:interaction_id>/', views.delete_interaction, name='delete_interaction'),

    path('inbox/', views.inbox, name='inbox'),
    path('notifications/', views.notifications, name='notifications'),
    path('chatrooms/', views.chatrooms, name='chatrooms'),
    path('<slug:slug>/', views.chatroom, name='chatroom'),
]
