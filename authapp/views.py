from django.shortcuts import render
from .forms import *


def auth_main(request):
    if request.method == 'GET':
        fields = UserProfileLoginForm
        return render(request, 'authapp/auth.html', {'fields': fields})
    else:
        pass


def auth_reg(request):
    if request.method == 'GET':
        fields = UserProfileRegisterForm
        return render(request, 'authapp/registration.html', {'fields': fields})
