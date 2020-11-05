from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django import forms
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# class UserManager(BaseUserManager):
    # def _create_user(self,username,password,email,**kwargs):
    #     if not password:
    #         raise ValueError("need password")
    #     if not username:
    #         raise ValueError("need username")
    #     if not email:
    #         raise ValueError("Mail Address")
    #     user = self.model(username=username,email=email,**kwargs)
    #     user.set_password(password)
    #     user.save()
    #     return user

    # def create_user(self, username, email, password=None):
    #     if not username:
    #         raise ValueError('Users must have an username')
    #     elif not email:
    #         raise ValueError('Users must have an email')

    #     user = self.model(
    #         username = username,
    #         email = self.normalize_email(email),
    #     )
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_superuser(self, username, email, password):
    #     user = self.create_user(
    #         username,
    #         email,
    #         password=password,
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user
        # kwargs['is_superuser'] = True
        # kwargs['is_staff'] = True
        # user
        # return self._create_user(username,password,email,**kwargs)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True,)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=18)
#     university = models.CharField(max_length=100)
#     research = models.TextField(max_length=300)
    
#     STATUS_GENDER = (
#         ('male', '男'),
#         ('female', '女'),
#         ('other', 'その他'),
#     )
#     gender = models.CharField(choices=STATUS_GENDER, default='male', max_length=10)
#     age = models.PositiveSmallIntegerField()
#     position = models.CharField(max_length=100)
#     self_introduction = models.TextField(max_length=300)
#     birthday = models.DateField(null=True, blank=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'password']
  
  
# https://hombre-nuevo.com/python/python0048/
class UserManager(BaseUserManager):
    """ユーザーマネージャー."""
  
    use_in_migrations = True
  
    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username, email, and
        password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email) #BaseUserManager に定義されている
  
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
  
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
  
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
  
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
  
        return self._create_user(email, password, **extra_fields)
  
  
class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""
  
    email = models.EmailField(_('email address'), unique=True)
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=150, blank=True)
    name = models.CharField(max_length=50)
  
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    university = models.CharField(max_length=100)
    research = models.TextField(max_length=300, null=True, blank=True)
    
    STATUS_GENDER = (
        ('male', '男'),
        ('female', '女'),
        ('other', 'その他'),
    )
    gender = models.CharField(choices=STATUS_GENDER, default='male', max_length=10)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    position = models.CharField(max_length=100)
    self_introduction = models.TextField(max_length=300, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
  
    objects = UserManager()
  
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
  
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
  
    # def get_full_name(self):
    #     """Return the first_name plus the last_name, with a space in
    #     between."""
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()
  
    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name
  
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
