from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Invitation
from .serializers import UserSerializer, InvitationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    filter_fields = ('author', 'place', 'date', 'status',)

    # フィールド一つだけ取得みたいなこともできる（/inv/{id}/date/）
    @action(methods=['get'], detail=True)
    def date(self, request, pk=None):
        inv = self.get_object()
        return Response('{inv.date}'.format(inv=inv))

    # 申請ボタンを押すと呼ばれる想定(PUT /inv/{id}/request/)
    @action(methods=['put'], detail=True)
    def request(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'requested'
        inv.save()
        print(inv)
        return Response('requested!')

    # 承認ボタンを押すと呼ばれる想定(PUT /inv/{id}/accept/)
    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'accepted'
        inv.save()
        print(inv)
        return Response('accepted!')

    # キャンセルボタンを押すと呼ばれる想定(PUT /inv/{id}/cancel/)
    @action(methods=['put'], detail=True)
    def cancel(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'seeking'
        inv.save()
        print(inv)
        return Response('canceled!')
