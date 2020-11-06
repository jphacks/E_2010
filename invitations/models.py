from django.db import models
from django.utils import timezone

from users.models import User

# Create your models here.
class Invitation(models.Model):
    author = models.ForeignKey(User, related_name='invitations', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField()
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100, null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
