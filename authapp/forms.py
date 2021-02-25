from django import forms
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm


class UserProfileLoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserProfileLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.HiddenInput(attrs={'class': 'form-control d-print-none'}),
        }
