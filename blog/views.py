from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Tag


# Create your views here.
def base_page(request):
    return render(request, 'blog/main.html')


class IndexPostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostByTag(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tag: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context