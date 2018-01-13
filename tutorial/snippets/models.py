from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    # additional
    point = models.FloatField(default=0.0)
    connect_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

