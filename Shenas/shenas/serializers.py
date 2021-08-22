from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'email']

    def validate_password(self, password):
        return make_password(password)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'email']
        read_only_fields = ['username']
