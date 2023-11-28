from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import UserProfile

def homeView(request):
    return render(request, 'home.html')
    
def loginView(request):
    if request.user.is_authenticated:
        messages.success(request, 'You already are logged in')
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username.lower())
        except:
            print('Wrong username')
            messages.error(request, 'You entered a wrong username')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Wrong password')
            messages.error(request, 'You entered a wrong password')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('home')

def registerView(request):
    if request.user.is_authenticated:
        messages.success(request, 'You already are logged in')
        return redirect('home')

    return render(request, 'register.html')