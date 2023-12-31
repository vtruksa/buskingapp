from django.db import models
from django.contrib.auth.models import User

from show.models import Show

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    art_name = models.CharField(max_length=128, null=True)
    gear = models.TextField(null=True)
    bio = models.TextField(null=True)
    link_ig = models.CharField(max_length=128, null=True)
    link_fb = models.CharField(max_length=128, null=True)
    link_x = models.CharField(max_length=128, null=True)
    link_tt = models.CharField(max_length=128, null=True)
    id_number = models.TextField(null=False, default=-1)
    # Warnings
    
    def __str__(self):
        if art_name is not null and art_name != '':
            return art_name
        return user.username
