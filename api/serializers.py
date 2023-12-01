from rest_framework import serializers
from django.contrib.auth.models import User
from show.models import *

class SpotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    lan = serializers.FloatField()
    lon = serializers.FloatField()
    name = serializers.CharField()
    description = serializers.CharField()
    allowedSlots = serializers.CharField()

    class Meta:
        model = Spot

class TimeSlotSerializer(serializers.Serializer):
    start=serializers.TimeField()
    end=serializers.TimeField()
    id=serializers.IntegerField()

    class Meta:
        model = TimeSlot
        fields = '__all__'

class ShowSerializer(serializers.Serializer):
    time=TimeSlotSerializer()
    artist=serializers.SerializerMethodField()
    spot=serializers.SerializerMethodField()
    date=serializers.DateField()
    id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        self.logged_user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def get_spot(self, obj):
        return obj.spot.name

    def get_artist(self, obj):
        print('Checking ' + str(obj.spot.name) + ' at ' + str(obj.time) + '; ' + str(obj.date))
        if obj.artist != None: 
            return obj.artist.id
        if Show.objects.filter(artist=self.logged_user, date=obj.date, time=obj.time).exists(): 
            return 0
        if Show.objects.filter(artist=self.logged_user, date=obj.date, spot=obj.spot).exists(): 
            return 0
        
        return -1 

    class Meta:
        model = Show
        fields = '__all__'

class ArtistSerializerMini(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'id']