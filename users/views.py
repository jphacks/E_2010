from django.shortcuts import render
from django.contrib.auth import get_user_model
from .form import RegisterForm, LoginForm
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
import json
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# User = get_user_model()
class RegisterProfile(APIView):
    def post(self, request):
        User = get_user_model()
        # print('request: ', request.POST.get('email', None))
        datas = json.loads(request.body)
        form = RegisterForm(datas)
        # if request.method == "POST":
        if form.is_valid():
            Username = form.cleaned_data["username"]
            Password = form.cleaned_data["password"]
            Useremail = form.cleaned_data["email"]
            username_exists = User.objects.filter(username=Username).exists()
            if username_exists:
                return JsonResponse({"code":400,"message":"username exists"})
            email_exists = User.objects.filter(email=Useremail).exists()
            if email_exists:
                return JsonResponse({"code":400,"message":"email exists"})

            UserData = User.objects.create_user(username=datas['username'],password=datas['password'],email=datas['email'], university = datas['university'], research = datas['research'], sex = datas['sex'],position = datas['position'], self_introduction = datas['self_introduction'], birthday = datas['birthday'])
            return JsonResponse({"id": UserData.id, "Username": UserData.username})
        else:
            return JsonResponse({"code":400,"message":"form worong"})
    def get(self, request):
        return Response("Get NOT ALLOWED")
        # return Response({"test": "Hello!"})

# {"email": "hogehoge2@hoge.com" ,"username": "hogdaedahoge2",  "password": "hogehoge", "university": "hogehoge" , "research": "research",  "sex": "male", "position": "Prof", "self_introduction": "hogehoge", "birthday":  "2020-11-02" }

class LoginView(APIView):
    def post(self, request):
        datas = json.loads(request.body)
        print(datas)
        form = LoginForm(datas)
        print(form.is_valid())
        if form.is_valid():
            Email = form.cleaned_data.get("email")
            Password = form.cleaned_data.get("password")
            Username = datas['username']
            print('UserName: ', Username)
            print('Email: ', Email)
            print('Password: ', Password)
            UserInfo = authenticate(username=Username,password=Password)
            print('UserInfo: ', UserInfo)
        return Response("ALLOWED")
    def get(self, request):
        return Response("Get NOT ALLOWED")
#{ "email": "hogehoge@hoge.com" ,"username": "hogdaedahoge",  "password": "hogehoge" }
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return JsonResponse({"code": 200})
    def get(self, request):
        return Response("Get NOT ALLOWED")

def MergeDict(OriDict, ReqDict): 
    MergedDict = {}
    for key in OriDict:
        if key in ReqDict:
            MergedDict[key] = ReqDict.get(key)
        else:
            MergedDict[key] = OriDict.get(key)
    return MergedDict
class UserManagmentView(APIView):
    def post(self, request):
        return JsonResponse({"code": 200})
    def get(self, request):
        return Response("Get NOT ALLOWED")
    def put(self, request):
        RequestData = json.loads(request.body)
        User = get_user_model()
        if 'id' not in RequestData:
            return JsonResponse({"code": 200})
        else:
            UpdateID = RequestData['id']
            del RequestData['id']
            if len(RequestData) == 0:
                print('Error')
                return JsonResponse({"code": 200})
        OriDict = User.objects.filter(id=UpdateID).values().first()
        UpdateDict = MergeDict(OriDict, RequestData)
        User.objects.filter(id=UpdateID).update(email = UpdateDict['email'], username = UpdateDict['username'], university = UpdateDict['university'], research = UpdateDict['research'], sex = UpdateDict['sex'], position = UpdateDict['position'], self_introduction = UpdateDict['self_introduction'], birthday = UpdateDict['birthday'], password = UpdateDict['password'])
        
        return JsonResponse({"code": 200})
    def delete(self, request):
        RequestData = json.loads(request.body)
        User = get_user_model()
        if 'id' not in RequestData:
            return JsonResponse({"code": 200})
        else:
            User.objects.filter(id=RequestData['id']).delete()
            return JsonResponse({"code": 200})

#{"id": "25", "university": "hogeUniv"}
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Approve(APIView):
    def post(self, request):
        datas = json.loads(request.body)
        invitation = datas['invitationid']
        applicant = datas['applicantid']
        # Apply = Application.Manager()
        # print(invitationID)
        # print(applicantid)
        Application.objects.update_or_create(invitationid = invitation, applicantid = applicant, Status = 'approve')    #should only do update
        return JsonResponse({"hoge": "hoge"})

    # def get(self, request):
    #     return Response({"404": "GET NOT ALLOWED"})

class Apply(APIView):
    def post(self, request):
        datas = json.loads(request.body)
        invitation = datas['invitationid']
        applicant = datas['applicantid']
        # Apply = Application.Manager()
        # print(invitationID)
        # print(applicantid)
        Application.objects.update_or_create(invitationid = invitation, applicantid = applicant, Status = 'pending')
        return JsonResponse({"hoge": "hoge"})

    # def get(self, request):
    #     return Response({"404": "GET NOT ALLOWED"})

class Deny(APIView):
    def post(self, request):
        datas = json.loads(request.body)
        invitation = datas['invitationid']
        applicant = datas['applicantid']
        # Apply = Application.Manager()
        # print(invitationID)
        # print(applicantid)
        Application.objects.update_or_create(invitationid = invitation, applicantid = applicant, Status = 'deny')     #should only do update
        return JsonResponse({"hoge": "hoge"})

    # def get(self, request):
    #     return Response({"404": "GET NOT ALLOWED"})
#{"invitationid": "22", "applicantid": "33"}