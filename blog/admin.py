from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug',)


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'created', 'get_photo', 'views')
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
