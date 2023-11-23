from django.db import models

# Create your models here.
class Spot(models.Model):
    lan = models.FloatField()
    lon = models.FloatField()
    #allowedSlots
    #municipality