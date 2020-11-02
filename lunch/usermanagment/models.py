from django.db import models

class Profile(models.Model):
    user_id = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    research = models.TextField(max_length=300)
    sex = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=100)
    self_introduction = models.TextField(max_length=300)
