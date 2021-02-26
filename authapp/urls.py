from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('login', views.auth_login, name='auth_login_url'),
    path('logout', views.auth_logout, name='auth_logout_url'),
    path('registration/', views.auth_reg, name='reg_url')
]
