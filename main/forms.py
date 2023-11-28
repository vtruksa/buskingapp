from django import forms

from .models import *

class UserProfileForm(forms.Form):
    class Meta:
        model = UserProfile
        exclude = ['user']