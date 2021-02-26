from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('details/<int:pk>', views.details, name='details')
]