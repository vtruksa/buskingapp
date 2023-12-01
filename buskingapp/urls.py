from django.contrib import admin
from django.urls import path, include

from main.views import *
from show.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", homeView, name="home"),
    path("manage-spot/", manageSpots, name="manage-spot"),
    path("logout/", logoutView, name="logout"),
    path("login/", loginView, name="login"),
    path("register/", registerView, name="register"),

    path("booking/", bookView, name="book"),
    path("show-list/", showView, name="show-list"),

    path('api/', include('api.urls')),
]
