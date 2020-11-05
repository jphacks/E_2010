from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_staff', 'name',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
