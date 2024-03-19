from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {"user": user})

def signin_view(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = SigninForm()
    return render(request, "signin.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect(request.META.get("HTTP_REFERER"))
