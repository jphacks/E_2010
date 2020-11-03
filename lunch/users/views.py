from django.shortcuts import render
from django.contrib.auth import get_user_model
# from .forms import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
import json
# Create your views here.
# class RegisterProfile(APIView):
#     def get(self, request, format=None):
#         snippets = Profile.objects.all()
#         serializer = ProfileSerializer
#         return Response({"test": "Hello!"})

# User = get_user_model()
class RegisterProfile(APIView):
    def post(self, request):
        User = get_user_model()
        # print('request: ', request.POST.get('email', None))
        datas = json.loads(request.body)
        if request.method == "POST":
            print('Username: ', self.request.POST.get('username', None))
            # print(username=request.POST.GET('username'))
            # print('User: ', request.body)
            User.objects.create_user(username=datas['username'],password=datas['password'],email=datas['email'], university = datas['university'], research = datas['research'], sex = datas['sex'],position = datas['position'], self_introduction = datas['self_introduction'], birthday = datas['birthday'])
            return JsonResponse({"hoge": "hoge"})
    def get(self, request):
        return Response({"test": "Hello!"})

# {"email": "hogehoge" ,"username": "hogehoge",  "password": "hogehoge", "university": "hogehoge" , "research": "research",  "sex": "male", "position": "Prof", "self_introduction": "hogehoge", "birthday":  "2020-11-02" }