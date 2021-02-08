from django.shortcuts import render


def auth_main(request):
    return render(request, 'authapp/auth.html')
