from django.db import models


# Create your models here.
class Pictures(models.Model):
    title = models.CharField(max_length=150)
    images = models.ImageField(upload_to='photos/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'Pictures'
        verbose_name = 'Picture'

    def __str__(self):
        return self.title
