from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    content = models.TextField(blank=True)
    url = models.TextField(unique=True, verbose_name='источник')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True, blank=True)

    def __str__(self):
        return self.title
