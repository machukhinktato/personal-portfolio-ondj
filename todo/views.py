from django.shortcuts import render


def todo_main(request):
    return render(request, 'todo/todo_main.html')
