from django import forms
from posts.models import Post, Tag


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


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search',
                'class': 'form-control',
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    orderings = (
        ('title', 'по заголовку'),
        ('-title', 'по заголовку в обратном порятке'),
        ('rate', 'по рейтингу'),
        ('-rate', 'по рейтингу в обратном порятке'),
        ('-created_at', 'по дате создания в обратном порятке'),
        ('created_at', 'по дате создания')
    )
    orderings = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'placeholder': 'Ordering', 'class': 'form-control'})
    )


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'rate']


class CommentForm(forms.Form):
    text = forms.CharField(label='Comment', max_length=300)
