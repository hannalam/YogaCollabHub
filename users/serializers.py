from rest_framework import serializers
from .models import Profile, Tutor
from session.models import ClassType, YogaClass
from enrollment.models import Enrollment
from interactions.models import Yogahub, ChatRoom, ChatRoomMessage, Message, Notification

class ProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_photo','bio', 'location']

class TutorSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Tutor
        fields = ['id', 'user', 'profile_photo','bio', 'location']

class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ['id', 'name']

class YogaClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = YogaClass
        fields = ['id', 'title', 'class_type', 'tutor', 'date', 'time', 'classroom_equipment', 'description', 'location', 'enrolled_students','image_material','audio_material','video_material']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'session', 'enrollment_date']

class YogahubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yogahub
        fields = ['id', 'user', 'image', 'title', 'caption', 'date']

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'slug']

class ChatRoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomMessage
        fields = ['id', 'user', 'chatroom', 'messages', 'date']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'timestamp']