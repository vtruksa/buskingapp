from django.contrib import admin
from django.urls import path, include

from main.views import *
from show.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", homeView, name="home"),
    path("logout/", logoutView, name="logout"),
    path("login/", loginView, name="login"),
    path("register/", registerView, name="register"),
    path("user-edit/", userEdit, name="user-edit"),
    path("contact/", contactView, name="contact"),

    path("manage-spot/", manageSpots, name="manage-spot"),
    path("booking/", bookView, name="book"),
    path("my-shows/", showView, name="show-list"),
    path("shows/", showList, name="shows"),

    path("feedback/", feedback, name="feedback"),
    path("feedback/<int:pk>", feedbackView, name="feedback-r"),
    path("artist-overview/", artistOverview, name="artist-overview"),
    path("artist/<int:pk>", artistView, name="artist"),

    path('api/', include('api.urls')),
]
