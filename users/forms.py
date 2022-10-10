from django import forms
from .models import AppUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class AppUserForm(forms.ModelForm):
    class Meta:
        model=AppUser
        fields=['gender','address','mobile','city','pincode']
