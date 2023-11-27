from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spot(models.Model):
    lan = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=125, null=False, default='')
    description = models.TextField(null=True)
    allowedSlots = models.CharField(max_length=50, null=False, default='')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)