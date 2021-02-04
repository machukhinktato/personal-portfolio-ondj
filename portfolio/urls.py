from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('<int:pk>', views.project_details, name='project_details'),
]