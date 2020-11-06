from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'university', 'research', 'gender', 'age', 'position', 'self_introduction', 'birthday')
        extra_kwargs = {
            'password': {'write_only': True},
        }
