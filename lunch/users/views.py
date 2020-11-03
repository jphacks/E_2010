from django.shortcuts import render
from django.contrib.auth import get_user_model
# from .forms import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
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
        if request.method == "POST":
            print('Username: ', request.POST.get('username', None))
            # print(username=request.POST.GET('username'))
            User.objects.create_user(username=request.POST.get('username', None),password=request.POST.get('password'),email=request.POST.get('email'), university = request.POST.get('university'), research = request.POST.get('research'), sex = request.POST.get('sex'),position = request.POST.get('position'), self_introduction = request.POST.get('self_introduction'), birthday = request.POST.get('birthday'))
    def get(self, request):
        return Response({"test": "Hello!"})

# {"email": "hogehoge" ,"username": "hogehoge",  "password": "hogehoge", "university": "hogehoge" , "research": "research",  "sex": "male", "self_introduction": "hogehoge", "birthday":  "2020-11-02" }