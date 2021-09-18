from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Tag
from .forms import NewPost


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


def new_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('index_blog')
    else:
        form = NewPost()
    return render(request, 'blog/post_add.html', {'form': form})
