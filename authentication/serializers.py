from rest_framework import serializers
from admin_cinema.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(max_length=68, min_length=6, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        password_confirm = attrs.get('password_confirm', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')

        if password != password_confirm:
            raise serializers.ValidationError('The passwords do not match')

        return attrs

    def create(self, validated_data):
        # Remove the 'password_confirm' field before creating the user
        validated_data.pop('password_confirm', None)
        request = self.context.get('request')
        return User.objects.create_user(request=request, **validated_data)