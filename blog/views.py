from django.shortcuts import render


def blog():
    return render(request, 'blog/blog.html')
