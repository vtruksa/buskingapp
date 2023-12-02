from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spot(models.Model):
    lan = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=125, null=False, default='')
    description = models.TextField(null=True)
    allowedSlots = models.CharField(max_length=300, null=False, default='')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shows_future = models.ManyToManyField('Show', related_name='show_f')
    shows_past = models.ManyToManyField('Show', related_name='show_p')

class Show(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.ForeignKey('TimeSlot', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.spot.name) + ' at ' + str(self.date) + ' ' + str(self.time)

class TimeSlot(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return str(self.start) + ' - ' + str(self.end)


class Feedback(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()