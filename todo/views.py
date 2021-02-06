from django.shortcuts import render
from .models import ToDoModel
from .forms import ToDoForm


def todo_main(request):
    todo_list = ToDoModel.objects.all()
    return render(request, 'todo/todo_main.html', {'todo_list': todo_list})


def todo_form_creation(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html', form=ToDoForm)
