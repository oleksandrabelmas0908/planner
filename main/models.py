from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Tasks(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time_it_takes = models.CharField(max_length=20)
    is_done = models.BooleanField(default=False)