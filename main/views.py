from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, UserForm

def homeView(request):
    context = {'profile':UserProfile.objects.get(user=request.user)}
    return render(request, 'home.html', context)
    
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
    if request.method == "POST":
        try:
            u = User.objects.create(
                username=request.POST.get('username').lower(),
                email=request.POST.get('email'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name')
            )
            u.set_password(request.POST.get('password'))
            u.save()
            # TODO encrypt
            id_number = request.POST.get('id_number')
            up = UserProfile.objects.create(
                user=u,
                id_number=id_number,
                gear=request.POST.get('gear'),
                bio=request.POST.get('bio'),
                link_ig=request.POST.get('link_ig'),
                link_fb=request.POST.get('link_fb'),
                link_x=request.POST.get('link_x'),
                link_tt=request.POST.get('link_tt')
            )

            login(request, u)
            return redirect('home')
        except Exception as e: 
            print('There was an error during the registration proccess: ' + str(e))
            messages.error(request, 'There was an error during the registration proccess')

    context = {
        'f1': UserForm(),
        'f2': UserProfileForm()
    }

    return render(request, 'register.html', context)

def userEdit(request):
    context = {}
    return render(request, 'user_edit.html', context)