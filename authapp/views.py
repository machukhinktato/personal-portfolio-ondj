from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.conf import settings
from .forms import *


def auth_login(request):
    title = 'вход'
    fields = UserProfileLoginForm(data=request.POST or None)
    _next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST' and fields.is_valid():
        # username = fields.cleaned_data['username']
        # password = fields.cleaned_data['password']
        user = auth.authenticate(
            username=fields.cleaned_data['username'],
            password=fields.cleaned_data['password'])
        if user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    content = {
        'title': title,
        'fields': fields,
        'next': _next,
    }
    return render(request, 'authapp/auth.html', content)


def auth_reg(request):

