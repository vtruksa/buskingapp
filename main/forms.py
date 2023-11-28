from django import forms
from django.contrib.auth.models import User

from .models import *

class UserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="Uživatelské jméno")
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=50, required=True, label="Křestní jméno")
    last_name = forms.CharField(max_length=50, required=True, label="Příjmení")
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserProfileForm(forms.Form):
    id_number = forms.CharField(max_length=12, required=True, label="Číslo identifikačního dokladu (op, pas, ř.p.)")
    gear = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Výbava a nástroje')
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Bio')
    link_ig = forms.CharField(max_length=128, label="Link na Instagram")
    link_fb = forms.CharField(max_length=128, label="Link na Facebook")
    link_x = forms.CharField(max_length=128, label="Link na X")
    link_tt = forms.CharField(max_length=128, label="Link na TikTok")

    class Meta:
        model = UserProfile
        exclude = ['user']