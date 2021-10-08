from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug',)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'created', 'get_photo')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('tags',)
    readonly_fields = ('created', 'get_photo')
    fields = ('title', 'slug', 'tags', 'content', 'photo', 'get_photo', 'created', 'author')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
