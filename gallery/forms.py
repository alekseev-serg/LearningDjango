from django import forms
from .models import Pictures


class LoadForm(forms.ModelForm):
    class Meta:
        model = Pictures

        fields = ['images']
        widgets = {
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
