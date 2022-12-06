from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class blog(models.Model):
    content = models.TextField(max_length=300, default='')
    dateTime = models.DateTimeField(default=timezone.now)
    usrName = models.ForeignKey(User, on_delete=models.CASCADE)


class comment(models.Model):
    comment = models.TextField(max_length=300, default='')
    like = models.IntegerField(default=0)
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, null=True, blank=True, default=None)
