from django.shortcuts import render
from .forms import UserProfileLoginForm


def auth_main(request):
    if request.method == 'GET':
        fields = UserProfileLoginForm
        return render(request, 'authapp/auth.html', {'fields': fields})
