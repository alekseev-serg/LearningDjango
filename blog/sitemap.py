from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9


    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)


class DynamicViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Post.objects.all()
