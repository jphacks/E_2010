from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm  # 追記
from django.urls import reverse_lazy
from . import forms
# Create your views here.
def loginfunction(request):
    return render(request, 'login/login.html')

# @csrf_protect
# @api_view(["GET","POST"])
def loginform(request):
    print(request)
    # return render(request, 'index.html')
    if request.method =="GET":
        username = request.GET.get("email")
        pwd = request.GET.get("password")
    elif request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        print('username: ', username)
        print('PW: ', pwd)
    else:
        return render(request,template_name="index.html",context={"msg":"Error"})
    if username  is not None and pwd is not  None:
        print('redirect')
        if username =='admin'and pwd == "admin":
            return  render(request,"index.html")
        else:
            # return render(request, "index.html", context={"msg": "Input Error"})
            return redirect('index.html')
    else:
        print('Nonredirect')
        request.sessions.flush()
        return redirect('login/login.html')
        # return  render(request,"login.html",context={"msg":"Need User name and Password"})

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "login/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout/logout.html"

class IndexView(TemplateView):
    template_name = "index.html"

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "create/create.html"
    success_url = reverse_lazy("login")