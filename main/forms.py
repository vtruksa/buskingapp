from django import forms
from django.contrib.auth.models import User

from .models import *

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, label="Uživatelské jméno")
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=50, required=True, label="Křestní jméno")
    last_name = forms.CharField(max_length=50, required=True, label="Příjmení")
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=50, required=True, label="Křestní jméno")
    last_name = forms.CharField(max_length=50, required=True, label="Příjmení")
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    id_number = forms.CharField(max_length=12, required=True, label="Číslo identifikačního dokladu (op, pas, ř.p.)")
    gear = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Výbava a nástroje', required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Bio', required=False)
    link_ig = forms.CharField(max_length=128, label="Link na Instagram", required=False)
    link_fb = forms.CharField(max_length=128, label="Link na Facebook", required=False)
    link_x = forms.CharField(max_length=128, label="Link na X", required=False)
    link_tt = forms.CharField(max_length=128, label="Link na TikTok", required=False)

    class Meta:
        model = UserProfile
        exclude = ['user']