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
    invitation = InvitationSerializer(read_only=True)
    inv_id = serializers.PrimaryKeyRelatedField(queryset=Invitation.objects.all(), write_only=True)
    

    class Meta:
        model = Application
        fields = ('id', 'invitation', 'inv_id', 'applicant', 'status',)

    def create(self, validated_data):
        validated_data['invitation'] = validated_data.get('inv_id', None)
        if validated_data['invitation'] is None:
            raise serializers.ValidationError("invitation not found")
        del validated_data['inv_id']
        # validated_data['status'] = 'seeking'
        return Application.objects.create(**validated_data)
