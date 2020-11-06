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

    # 拒否ボタンを押すと呼ばれる想定(PUT /api/applications/{id}/deny/)
    # @action(methods=['put'], detail=True)
    # def deny(self, request, pk=None):
    #     app = Application.objects.filter(id=self)

# class Approve(APIView):
#     def post(self, request):
#         datas = json.loads(request.body)
#         invitation = datas['invitationid']
#         applicant = datas['applicantid']
#         # Apply = Application.Manager()
#         # print(invitationID)
#         # print(applicantid)
#         Application.objects.update_or_create(invitationid = invitation, applicantid = applicant, Status = 'approve')    #should only do update
#         return JsonResponse({"hoge": "hoge"})

#     # def get(self, request):
#     #     return Response({"404": "GET NOT ALLOWED"})

# class Apply(APIView):
#     def post(self, request):
#         datas = json.loads(request.body)
#         invitation = datas['invitationid']
#         applicant = datas['applicantid']
#         # Apply = Application.Manager()
#         # print(invitationID)
#         # print(applicantid)
#         Application.objects.update_or_create(invitationid = invitation, applicantid = applicant, Status = 'pending')
#         return JsonResponse({"hoge": "hoge"})

#     # def get(self, request):
#     #     return Response({"404": "GET NOT ALLOWED"})

# class Deny(APIView):
#     def post(self, request):
#         datas = json.loads(request.body)
#         invitation = datas['invitationid']
#         applicant = datas['applicantid']
#         # Apply = Application.Manager()
#         # print(invitationID)
#         # print(applicantid)
#         Application.objects.update_or_create(invitationid = invitation, applicantid = applicant, Status = 'deny')     #should only do update
#         return JsonResponse({"hoge": "hoge"})

#     # def get(self, request):
#     #     return Response({"404": "GET NOT ALLOWED"})
# #{"invitationid": "22", "applicantid": "33"}