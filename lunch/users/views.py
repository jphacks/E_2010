from django.shortcuts import render
from django.contrib.auth import get_user_model
from .form import RegisterForm, LoginForm
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
import json
from django.contrib.auth import authenticate
from django.contrib.auth import login
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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    