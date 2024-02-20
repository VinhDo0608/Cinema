# serializers.py
from rest_framework import serializers
from admin_cinema.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_verified', 'is_active', 'is_staff', 'create_at', 'update_at']
