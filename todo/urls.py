from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_main, name='todo_url'),
]