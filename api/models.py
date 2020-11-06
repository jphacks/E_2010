from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
  
# User ###################################################

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
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # 未使用
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # USERNAME_FIELD = 'id' としたことによるエラーの対処法
    # https://teratail.com/questions/98546
    def __str__(self):
        return str(self.id)

###########################################################


# Invitation ##############################################

class Invitation(models.Model):
    author = models.ForeignKey(User, related_name='invitations', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField()
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100, null=True, blank=True)
    
    STATUS = (
        ('seeking', '募集中'),
        ('applied', '承認待ち'),
        ('accepted', '承認済み'),
    )
    status = models.CharField(choices=STATUS, default='seeking', max_length=10)

    def __str__(self):
        return str(self.id)

###########################################################


# Application ##############################################
class Application(models.Model):
    # authorid = models.CharField(max_length=128)    #userid
    invitation = models.ForeignKey(Invitation, related_name='applications', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    APPLICATION_STATUS = (
      ('applied', '承認待ち'),
      ('accepted', '承認済み'),
      ('denied', '拒否'),
    )
    status = models.CharField(choices=APPLICATION_STATUS, max_length=10)
    