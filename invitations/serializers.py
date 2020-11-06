from rest_framework import serializers

from .models import Invitation
from users.models import User
from users.serializers import UserSerializer

# GET 時は User の中身を見たい、かつ POST 時は id だけ指定したい
# https://sakataharumi.hatenablog.jp/entry/2018/10/20/010806
class InvitationSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Invitation
        fields = ('id', 'author', 'user_id', 'title', 'content', 'date', 
                    'place', 'created_at', 'tags', 'is_accepted',)
        read_only_fields = ('author', 'created_at', 'is_accepted',)

    def create(self, validated_data):
        validated_data['author'] = validated_data.get('user_id', None)
        if validated_data['author'] is None:
            raise serializers.ValidationError("author not found")
        del validated_data['user_id']
        validated_data['is_accepted'] = False
        return Invitation.objects.create(**validated_data)