from django.contrib import admin
from django.urls import path

from main.views import *
from show.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path("manage-spot/", manageSpots, name="manage-spot"),
]
