from os import stat_result
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=now, blank=True)
    end_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
