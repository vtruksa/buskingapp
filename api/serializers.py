from rest_framework import serializers

class SpotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    lan = serializers.FloatField()
    lon = serializers.FloatField()
    name = serializers.CharField()
    description = serializers.CharField()
    allowedSlots = serializers.CharField()