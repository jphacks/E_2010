from rest_framework import serializers

from .models import User, Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # password はあとで消す
        fields = ('email', 'name', 'password', 
                    'university', 'research', 'gender', 
                    'age', 'position', 'self_introduction', 'birthday')
