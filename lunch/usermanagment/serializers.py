from rest_framework import serializers
# from profile import Profile


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('user_id', 'university', 'research',
#                   'sex', 'position', 'self_introduction')

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'university', 'research','sex', 'position', 'self_introduction']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']