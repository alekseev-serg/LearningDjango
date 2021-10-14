from django.db import models
from django.urls import reverse

from time import time
from pytils.translit import slugify

# Create your models here.
"""
Модель Post
Post - title, created, content, author, slug, photo, tags

Модель Tag
Tag - title, slug
"""


def tag_gen_slug(s):
    new_slug = slugify(s)
    return new_slug


def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = tag_gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100, default='admin')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created']
