from django.urls import path
from blog.views import *

urlpatterns = [
    path('', base_page, name='home'),
    path('blog/', IndexPostList.as_view(), name='index_blog'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('blog/tag/<str:slug>/', PostByTag.as_view(), name='tag'),
]
