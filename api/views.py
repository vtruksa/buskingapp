from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from show.models import Spot
from api.serializers import SpotSerializer

@api_view(('GET', ))
def getSpot(request):
    spot = Spot.objects.get(id=request.GET.get('id'))

    serializer = SpotSerializer(spot, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)