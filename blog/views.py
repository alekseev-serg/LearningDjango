from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Tag
from .forms import NewPost
from django.contrib.auth.decorators import login_required


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


@login_required
def post_new(request):
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('index_blog')
    else:
        form = NewPost()
    return render(request, 'blog/post_add.html', {'form': form})


@login_required
def post_edit(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', slug=slug)
    else:
        form = NewPost(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})


@login_required
def try_to_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_delete.html', {'post': post})


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('index_blog')
