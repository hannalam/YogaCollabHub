from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('newpost/', views.new_post, name='new_post'),
    path('yogahub/', views.yogahub, name='yogahub'),
    path('notifications/', views.notifications, name='notifications'),
    path('chatrooms/', views.chatrooms, name='chatrooms'),
    path('<slug:slug>/', views.chatroom, name='chatroom'),


]
