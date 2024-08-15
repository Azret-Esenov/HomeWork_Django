from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post


def home_work(request):
    if request.method == 'GET':
        return HttpResponse("Hello Teacher!")


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')


def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', context={'post': post})


def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'post_create.html')
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST.get('title')
        content = request.POST.get('content')
        rate = request.POST.get('rate')
        Post.objects.create(
            image=image,
            title=title,
            content=content,
            rate=rate,
        )
        return redirect('/posts/')
