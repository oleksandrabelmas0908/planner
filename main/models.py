from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time_it_takes = models.CharField(max_length=20)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
