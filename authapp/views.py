from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.conf import settings
from .forms import *


def auth_login(request):
    title = 'вход'
    auth_form = UserProfileLoginForm(data=request.POST or None)
    _next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST' and auth_form.is_valid():
        # username = fields.cleaned_data['username']
        # password = fields.cleaned_data['password']
        user = auth.authenticate(
            username=auth_form.cleaned_data['username'],
            password=auth_form.cleaned_data['password'])
        if user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main:index'))

    content = {
        'title': title,
        'auth_form': auth_form,
        'next': _next,
    }
    return render(request, 'authapp/auth.html', content)


def auth_logout(request):
    title = 'выход'
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def auth_reg(request):
    pass
#     title = 'регистрация'
#     reg_form = ''
