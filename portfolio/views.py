from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    content = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', content)
