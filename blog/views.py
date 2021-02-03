from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html')


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/details.html')



# https://github.com/zappycode/django3-personal-portfolio/blob/master/blog/views.py