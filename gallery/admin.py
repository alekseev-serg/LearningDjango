from django.contrib import admin
from .models import Pictures


class PicAdmin(admin.ModelAdmin):
    list_display = ('title', 'images',)


# Register your models here.
admin.site.register(Pictures, PicAdmin)
