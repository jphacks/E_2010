from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse

from .models import User, Invitation, Application
from .serializers import UserSerializer, InvitationSerializer, ApplicationSerializer

import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=True)
    def login(self, request, pk=None):
        datas = json.loads(request.body)
        emailAdd = datas['email']
        Result = User.objects.filter(email=emailAdd).first()
        print(Result.id)
        
        return JsonResponse({'UserID': Result.id})

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
    def apply(self, request, pk=None):
        print(request.body)
        datas = json.loads(request.body)
        applicantID = datas['applicant']
        invitationID = datas['inv_id']
        # もしなかったら
            # 作成する
        # もしあったら
            #もう存在しているよと返す。（承認されてるのにまた応募するのがへんです、もうすでに承認待ちの状態であれば更新する必要がない。
        Author = Invitation.objects.filter(id = invitationID).first()
        print('Author.author_id: ', Author.author_id)
        print('self.get_object().invitation: ', self.get_object().invitation)
        IsDenied = Application.objects.filter(invitation = self.get_object().invitation, applicant = self.get_object().applicant).first()
        print("Isdenied: ", IsDenied)
        if Author.author_id == applicantID:
            return Response('You can not apply the Invitation that post by youself')
        if IsDenied.status == 'denied':
            return Response('This User is denied for this Invitation')    #deniedされたユーザを拒否する
        if IsDenied.status == 'applied' or IsDenied.status == 'accepted':
            return Response('This User is already applied for this Invitation. ')
        Application.objects.create(invitation = self.get_object().invitation, applicant = self.get_object().applicant, status = 'applied')
        return Response('applied!')

    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        app = Application.objects.filter(id = self.get_object().id).first()
        if app.status == 'denied':
            return Response('This User is denied for this Invitation')    #deniedされたユーザを拒否する
        app.status = 'accepted'
        app.save()
        return Response('accepted!')

    @action(methods=['put'], detail=True)
    def deny(self, request, pk=None):
        app = Application.objects.filter(id = self.get_object().id).first()
        app.status = 'denied'
        app.save()
        return Response('denied!')

    @action(methods=['put'], detail=True)
    def delete(self, request, pk=None):
        app = Application.objects.filter(id = self.get_object().id).first()
        app.delete()
        return Response('canceled!')

# Application Table
# |id|invitaion|applicant|status|
# |1|1         |2        |applied|
# |2|1         |3        |applied|

# GET /api/applications/ -> all
# GET /api/applications/?invitaion=1/ -> 
