from django import forms
from .models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'slug', 'content', 'photo', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
