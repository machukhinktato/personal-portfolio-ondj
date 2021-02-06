from django.db import models
from django.contrib.auth.models import User


class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)
    high_priority = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
