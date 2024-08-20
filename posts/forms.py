from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'rate']
        widgets = {
            'image': forms.ClearableFileInput(
                attrs={
                    'multiple': False,
                    'placeholder': 'Upload image',
                    'rows': 10,
                    'cols': 20
                }),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                    'rows': 10,
                    'cols': 20
                }),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Content',
                    'rows': 10,
                    'cols': 20
                }),
            'rate': forms.NumberInput(
                attrs={
                    'placeholder': 'Rate',
                    'rows': 10,
                    'cols': 20
                })
        }
