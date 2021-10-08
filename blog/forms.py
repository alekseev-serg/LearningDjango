from django import forms
from .models import Post, Tag


class NewPost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'content', 'photo', 'tags']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'photo': 'Изображение',
            'tags': 'Тэги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag

        fields = ['title', ]
        labels = {
            'title': 'Введите название тэга'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
