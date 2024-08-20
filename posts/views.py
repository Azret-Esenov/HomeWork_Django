from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.forms import PostForm
from posts.models import Post


def home_work(request):
    if request.method == 'GET':
        return HttpResponse("Hello Teacher!")


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')


@login_required(login_url='login')
def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', context={'posts': posts})


@login_required(login_url='login')
def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', context={'post': post})


@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', {'form': form})

        image = form.cleaned_data.get('image')
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        rate = form.cleaned_data.get('rate')

        Post.objects.create(
            image=image,
            title=title,
            content=content,
            rate=rate,
        )
        return redirect('/posts/')
