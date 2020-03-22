from django.shortcuts import render

from blog.models import BlogPost


def blog_index(request):
    blogs = BlogPost.objects.order_by('-date')
    return render(request, 'blog/blog_index.html', {'blogs': blogs})
