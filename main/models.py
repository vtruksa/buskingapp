from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50, null=False)
    l_name = models.CharField(max_length=50, null=False)
    gear = models.TextField(null=True)
    bio = models.TextField(null=True)
    link_ig = models.CharField(max_length=128, null=True)
    link_fb = models.CharField(max_length=128, null=True)
    link_x = models.CharField(max_length=128, null=True)
    link_tt = models.CharField(max_length=128, null=True)
    
    # Warnings