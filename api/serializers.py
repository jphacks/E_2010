from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators

from .models import User, Invitation, Application


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'university', 'research', 'gender', 'age', 'position', 'self_introduction', 'birthday')
        extra_kwargs = {
            'password': {'write_only': True},
        }

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'invitationid', 'applicantid', 'Status')
        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }


# GET 時は User の中身を見たい、かつ POST 時は id だけ指定したい
# https://sakataharumi.hatenablog.jp/entry/2018/10/20/010806
class InvitationSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Invitation
        fields = ('id', 'author', 'user_id', 'title', 'content', 'date', 
                    'place', 'created_at', 'tags', 'status',)
        read_only_fields = ('author', 'created_at', 'status',)

    def create(self, validated_data):
        validated_data['author'] = validated_data.get('user_id', None)
        if validated_data['author'] is None:
            raise serializers.ValidationError("author not found")
        del validated_data['user_id']
        validated_data['status'] = 'seeking'
        return Invitation.objects.create(**validated_data)

class ApplicationSerializer(serializers.ModelSerializer):
    # ApplyID = ApplicationSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Application.objects.all(), write_only=True)

    class Meta:
        model = Application
        fields = ('id', 'invitationid', 'applicantid', 'Status')
        # read_only_fields = ('author', 'created_at', 'status',)

    def create(self, validated_data):
        validated_data['id'] = validated_data.get('invitationid', None)
        if validated_data['id'] is None:
            raise serializers.ValidationError("invitation not found")
        del validated_data['invitationid']
        validated_data['Status'] = 'seeking'
        return Application.objects.create(**validated_data)