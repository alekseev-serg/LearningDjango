from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import F, Q
from django.utils import timezone

from .models import Post, Tag
from .forms import NewPost, TagForm, UserLoginForm


# Create your views here.
def base_page(request):
    return render(request, 'blog/main.html')


def about(request):
    return render(request, 'blog/about.html')


def index_post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        btn = False
    else:
        posts = Post.objects.filter(created__lte=timezone.now()).order_by('-created')
        btn = True

    context = {'posts': posts, 'btn': btn}
    return render(request, 'blog/post_list.html', context)


# class IndexPostList(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     paginate_by = 10
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


class PostDetail(DetailView):
    model = Post

    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostByTag(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
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
            form.save()
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
            form.save()
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


@login_required
def tag_new(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            messages.success(request, 'Тэг "{}" успешно создан'.format(tag.title))
            return redirect('tag_new')
        else:
            messages.error(request, 'Тэг с таким названием уже существует')
    else:
        form = TagForm()
    return render(request, 'blog/tag_add.html', {'form': form, 'tags': tags})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login_page.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
