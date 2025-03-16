from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = models.CharField(max_length=30, unique=True, default=None, null=False)
    password = models.CharField(max_length=30, default=None, null=False)

    def __str__(self):
        return self.username


class Tasks(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time_it_takes = models.CharField(max_length=20)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
