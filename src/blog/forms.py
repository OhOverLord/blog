from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'preview']
        labels = {
            'title': 'Заголовок',
            'body': 'Основной текст',
            'preview': 'Превью'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-title-post', 'placeholder': 'Введите название статьи'}),
            'body': forms.Textarea(attrs={'class': 'input-body'}),
        }