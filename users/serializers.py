from rest_framework import serializers
from .models import Profile, Tutor
from session.models import ClassType, YogaClass
from enrollment.models import Enrollment
from interactions.models import Yogahub, ChatRoom, ChatRoomMessage, Message, Notification

# Serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_photo','bio', 'location']

# Serializer for Tutor model
class TutorSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Tutor
        fields = ['id', 'user', 'profile_photo','bio', 'location']

# Serializer for ClassType model
class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ['id', 'name']

# Serializer for YogaClass model
class YogaClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = YogaClass
        fields = ['id', 'title', 'class_type', 'tutor', 'date', 'time', 'classroom_equipment', 'description', 'location', 'enrolled_students','image_material','audio_material','video_material']

# Serializer for Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'session', 'enrollment_date']

# Serializer for Yogahub model
class YogahubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yogahub
        fields = ['id', 'user', 'image', 'title', 'caption', 'date']

# Serializer for ChatRoom model
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'slug']

# Serializer for ChatRoomMessage model
class ChatRoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomMessage
        fields = ['id', 'user', 'chatroom', 'messages', 'date']

# Serializer for Message model
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']

# Serializer for Notification model
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'timestamp']