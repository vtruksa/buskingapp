from django.contrib import admin
from django.urls import path, include

from main.views import *
from show.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path("manage-spot/", manageSpots, name="manage-spot"),

    path('api/', include('api.urls')),
]
