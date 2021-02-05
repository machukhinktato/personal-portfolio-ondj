from django.shortcuts import render


def todo_main(request):
    return render(request, 'todo_main.html')
