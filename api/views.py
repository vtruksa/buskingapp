from django.shortcuts import render
from django.contrib import messages

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from show.models import Spot, Show, TimeSlot
from api.serializers import SpotSerializer, ShowSerializer

@api_view(('GET', ))
def getSpot(request):
    spot = Spot.objects.get(id=request.GET.get('id'))

    serializer = SpotSerializer(spot, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('GET', ))
def delSpot(request):
    try:
        s = Spot.objects.get(id=request.GET.get('id'))
    except:
        print("Couldn't find the requested spot")
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    s.delete()
    return Response({}, status=status.HTTP_200_OK)

@api_view(('GET', ))
def loadShows(request):
    try:
        id = request.GET.get('id')
        
        spot = Spot.objects.get(id=id)
        shows = Show.objects.filter(spot=spot)
        
        serializer = ShowSerializer(shows, many=True, user=request.user)
    except Exception as e:
        print(e)
        messages.error(request, "You have to pass in a valid spot id")
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)