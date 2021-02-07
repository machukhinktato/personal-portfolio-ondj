from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import ToDoModel
from .forms import ToDoForm


def todo_main(request):
    todo_list = ToDoModel.objects.all()
    return render(request, 'todo/todo_main.html', {'todo_list': todo_list})


def todo_create(request):
    if request.method == 'GET':
        return render(request, 'todo/todo_create.html', {'form': ToDoForm})
    else:
        try:
            form = ToDoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('todo_in_work')
        except ValueError:
            return render(request, 'todo/todo_create.html',
                          {'form': ToDoForm(), 'error': 'Bad data passed in. Try again.'})


# def todo_in_work(request):
#     todo_list = ToDoModel.objects.filter(user=request.user, end__isnull=True)
#     return render(request, 'todo/todo_in_work.html', {'todo_list': todo_list})
