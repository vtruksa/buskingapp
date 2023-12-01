from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('get-spot/', getSpot),
    path('del-spot/', delSpot),
    path('load-shows/', loadShows),
]