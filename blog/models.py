from django.db import models
from django.urls import reverse

# Create your models here.
"""
Модель Post
Post - title, created, content, author, slug, photo, tags

Модель Tag
Tag - title, slug
"""


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created']
