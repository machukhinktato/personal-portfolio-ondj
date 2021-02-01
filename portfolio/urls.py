from django.urls import path
from . import views
from blog import views

urlpatterns =[
    path('', views.index, name='index'),
    path('', views.blog, name='blog'),

]