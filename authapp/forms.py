from django import forms
from .models import UserProfile


class UserProfileLoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
