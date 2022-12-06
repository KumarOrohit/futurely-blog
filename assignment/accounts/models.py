from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='OIP.jpg')
    bio = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username}'