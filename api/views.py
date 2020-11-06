from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Invitation, Application
from .serializers import UserSerializer, InvitationSerializer, ApplicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('email',)


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    filter_fields = ('author', 'place', 'date', 'status',)

    # フィールド一つだけ取得みたいなこともできる（/api/invitations/{id}/date/）
    @action(methods=['get'], detail=True)
    def date(self, request, pk=None):
        inv = self.get_object()
        return Response('{inv.date}'.format(inv=inv))

    # 応募するボタンを押すと呼ばれる想定(POST /api/invitations/{id}/apply/)
    @action(methods=['put', 'post'], detail=True)
    def apply(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'applied'
        inv.save()
        # application 作成
        user_id = request.data['user_id']
        user = User.objects.get(id=user_id)
        print('applied by {}'.format(user.email))
        app = Application.objects.create(invitation=inv, applicant=user, status='applied')
        print(app)
        return Response('applied!')

    # (PUT /api/invitations/{id}/accept/)
    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'accepted'
        inv.save()
        # application 更新
        applicant_id = request.data['applicant_id']
        applicant = User.objects.get(id=applicant_id)
        app = Application.objects.get(invitation=inv, applicant=applicant)
        app.status = 'accepted'
        app.save()
        print('{} is accepted'.format(applicant.email))
        return Response('accepted!')

    # 削除するボタンを押すと呼ばれる想定
    # DELETE /api/invitations/{id}/delete/
    @action(methods=['delete'], detail=True)
    def delete(self, request, pk=None):
        inv_id = self.get_object().id
        inv = Invitation.objects.get(id=inv_id)
        apps = inv.applications.all() #https://qiita.com/saka___21/items/d461072e6ea65630171a
        inv.delete()
        apps.delete()
        print('{} is deleted'.format(inv_id))
        return Response('deleted!')

    # (PUT /api/invitations/{id}/cancel/)
    @action(methods=['put'], detail=True)
    def cancel(self, request, pk=None):
        inv = Invitation.objects.filter(id=self.get_object().id).first()
        inv.status = 'seeking'
        inv.save()
        # application 削除
        user_id = request.data['user_id']
        user = User.objects.get(id=user_id)
        print('applied by {}'.format(user.email))
        app = Application.objects.create(invitation=inv, applicant=user, status='applied')
        print(app)
        return Response('canceled!')


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_fields = ('invitation', 'applicant', 'status',)

    # select * from api_application where applicant=me and status=denied
    # @action(methods=['post'], detail=True)
    # def apply(self, request):
    #     # もしなかったら
    #         # 作成する
    #     # もしあったら
    #     IsDenied = Application.objects.filter(invitation = self.get_object().invitation, applicantid = self.get_object().applicant)
    #     if IsDenied.status == 'denied':
    #         return Response('This User is denied for this Invitation')    #deniedされたユーザを拒否する
    #     Application.objects.create(invitation = self.get_object().invitation, applicantid = self.get_object().applicant, status = 'applied')
    #     return Response('applied!')

    # 承認するボタンを押すと呼ばれる想定
    # PUT /api/applications/{id}/accept/
    @action(methods=['put'], detail=True)
    def accept(self, request, pk=None):
        # application 更新
        applicant_id = request.data['applicant_id']
        applicant = User.objects.get(id=applicant_id)
        app = Application.objects.get(id = self.get_object().id)
        app.status = 'accepted'
        app.save()

        # accepted 以外の応募記録を削除
        inv = self.get_object().invitation
        num_app = Application.objects.filter(invitation=inv).exclude(status='accepted').delete()
        
        # invitation 更新
        inv.status = 'accepted'
        inv.save()
        print('{} is accepted'.format(applicant.email))
        return Response('accepted!')

    # 拒否するボタンを押すと呼ばれる想定
    # PUT /api/applications/{id}/deny/
    @action(methods=['put'], detail=True)
    def deny(self, request, pk=None):
        app_id = self.get_object().id
        app = Application.objects.get(id=app_id)
        app.status = 'denied'
        app.save()
        print('{} is denied'.format(app_id))
        return Response('denied!')

    # 応募キャンセルボタンを押すと呼ばれる想定
    # PUT /api/applications/{id}/cancel/
    @action(methods=['put'], detail=True)
    def cancel(self, request, pk=None):
        app_id = self.get_object().id
        app = Application.objects.get(id=app_id)
        inv = app.invitation
        print(inv)
        app.delete()
        # invitation の応募者が 0 人なら status=seeking
        num_applicant = Application.objects.filter(invitation=inv).count()
        print(num_applicant)
        if num_applicant == 0:
            inv.status = 'seeking'
            inv.save()

        print('{} is canceled'.format(app_id))
        return Response('canceled!')

# Application Table
# |id|invitaion|applicant|status|
# |1|1         |2        |applied|
# |2|1         |3        |applied|

# GET /api/applications/ -> all
# GET /api/applications/?invitaion=1/ -> 
# curl -X PUT -H "Content-Type: application/json" \
#      -d '{"applicant_id":1}' localhost:8000/api/applications/16/accept/
# curl -X POST -H "Content-Type: application/json" \
#     -d '{"user_id":1,"title":"fuga","content":"","date":"2020-12-10","place":"office","tags":"lunch"}' \
#     localhost:8000/api/invitations/?applicant=1\&status=applied/ | jq
# curl -X POST -H "Content-Type: application/json" \
#     -d '{"user_id":2}' localhost:8000/api/invitations/5/apply/