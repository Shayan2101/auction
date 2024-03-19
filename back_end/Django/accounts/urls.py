from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"
urlpatterns = [
    path("profile/", profile, name="profile"),
    path("signin/", signin_view, name="signin"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
]
