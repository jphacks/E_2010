from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Invitation, Application
from .serializers import UserSerializer, InvitationSerializer, ApplicationSerializer


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

    # 申請ボタンを押すと呼ばれる想定(PUT /api/invitations/{id}/request/)
    @action(methods=['put'], detail=True)
    def request(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'applied'
        inv.save()
        print(inv)
        return Response('applied!')

    # 承認ボタンを押すと呼ばれる想定(PUT /api/invitations/{id}/accept/)
    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'accepted'
        inv.save()
        print(inv)
        return Response('accepted!')

    # キャンセルボタンを押すと呼ばれる想定(PUT /api/invitations/{id}/cancel/)
    @action(methods=['put'], detail=True)
    def cancel(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'seeking'
        inv.save()
        print(inv)
        return Response('canceled!')


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_fields = ('invitation', 'applicant', 'status',)

    # select * from api_application where applicant=me and status=denied
    @action(methods=['post'], detail=True)
    def apply(self, request):
        # もしなかったら
            # 作成する
        # もしあったら
        IsDenied = Application.objects.filter(invitation = self.get_object().invitation, applicantid = self.get_object().applicant)
        if IsDenied.status == 'denied':
            return Response('This User is denied for this Invitation')    #deniedされたユーザを拒否する
        Application.objects.create(invitation = self.get_object().invitation, applicantid = self.get_object().applicant, status = 'applied')
        return Response('applied!')

    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        app = Application.objects.filter(id = self.get_object().id).first()
        app.status = 'accepted'
        app.save()
        return Response('accepted!')

    @action(methods=['put'], detail=True)
    def deny(self, request, pk=None):
        app = Application.objects.filter(id = self.get_object().id).first()
        app.status = 'denied'
        app.save()
        return Response('denied!')

# Application Table
# |id|invitaion|applicant|status|
# |1|1         |2        |applied|
# |2|1         |3        |applied|

# GET /api/applications/ -> all
# GET /api/applications/?invitaion=1/ -> 
