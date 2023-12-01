from datetime import datetime, timedelta
from show.models import Show, Spot, TimeSlot

def generate():
    now = datetime.now()
    temp = now

    while temp < now+timedelta(days=3):
        times = open('static/times.txt').read().split('\n')
        for t in TimeSlot.objects.all(): 
            for s in Spot.objects.all():
                Show.objects.create(
                    spot=s,
                    date=datetime(year = temp.year, month=temp.month, day=temp.day),
                    time=t,
                )
        temp += timedelta(days=1)
