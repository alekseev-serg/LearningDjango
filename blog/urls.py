from django.urls import path, include
from blog.views import *
from .sitemap import StaticViewSitemap, DynamicViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'dynamic': DynamicViewSitemap
}

urlpatterns = [
    path('', base_page, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('about/', about, name='about'),
    path('blog/', index_post_list, name='index_blog'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('blog/post_new/', post_new, name='post_new'),
    path('blog/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('blog/<str:slug>/edit/', post_edit, name='post_edit'),
    path('blog/<str:slug>/try_to_delete/', try_to_delete, name='try_to_delete'),
    path('blog/<str:slug>/delete/', post_delete, name='post_delete'),
    path('blog/tags/create/', tag_new, name='tag_new'),
    path('blog/tag/<str:slug>/', PostByTag.as_view(), name='tag'),
]
