from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django import forms
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self,username,password,email,**kwargs):
        print(username)
        if not password:
            raise ValueError("need password")
        if not username:
            raise ValueError("need username")
        if not email:
            raise ValueError("Mail Address")
        user = self.model(username=username,email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,email,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username,password,email,**kwargs)

    def create_superuser(self,username,password,email,**kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username,password,email,**kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    university = models.CharField(max_length=100)
    research = models.TextField(max_length=300)
    STATUS_GENDER = (
      ('male', '男'),
      ('female', '女'),
      ('other', 'その他'),
  )
    sex = models.CharField(choices=STATUS_GENDER, default='male', max_length=10)
    # sex = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=100)
    self_introduction = models.TextField(max_length=300)
    birthday = models.DateField(null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']