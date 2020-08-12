from rest_framework import serializers
from rest_auth.models import TokenModel
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password2 = None

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])

    def validate(self, data):
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CustomTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = ('token', 'user')
