from django.shortcuts import render
from .models import *


# Create your views here.
def base_page(request):
    name = 'World'
    return render(request, 'blog/main.html', {'name': name})


def index_blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
