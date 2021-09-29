from django.urls import path
from blog.views import *

urlpatterns = [
    path('', base_page, name='home'),
    path('blog/', IndexPostList.as_view(), name='index_blog'),
    path('blog/post_new/', post_new, name='post_new'),
    path('blog/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('blog/<str:slug>/edit/', post_edit, name='post_edit'),
    path('blog/<str:slug>/try_to_delete/', try_to_delete, name='try_to_delete'),
    path('blog/<str:slug>/delete/', post_delete, name='post_delete'),
    path('blog/tag/<str:slug>/', PostByTag.as_view(), name='tag'),
]
