from django import forms
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm


class UserProfileLoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
            # 'password': forms.PasswordInput(
            #     attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'}),
        }


class UserProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.HiddenInput(attrs={'class': 'form-control d-print-none'}),
        }
