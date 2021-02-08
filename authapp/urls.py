from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('', views.auth_main, name='auth_main_url')
]
