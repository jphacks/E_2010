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
            print(username=request.POST.GET('username'))
            User.objects.create_user(username=request.POST.GET('username'),password=request.POST.GET('password'),email=request.POST.GET('email'))
    def get(self, request):
        return Response({"test": "Hello!"})