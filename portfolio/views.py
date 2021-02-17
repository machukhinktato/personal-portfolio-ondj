from django.shortcuts import render
from .models import Project


def about(request):
    return render(request, 'base.html')

def index(request):
    projects = Project.objects.all()
    content = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', content)


def project_details(request, pk):
    return render(request, 'portfolio/project_details.html', {'pk': pk})
