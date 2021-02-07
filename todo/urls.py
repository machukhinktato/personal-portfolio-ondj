from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_main, name='todo_url'),
    path('create/', views.todo_create, name='todo_create_url')
]