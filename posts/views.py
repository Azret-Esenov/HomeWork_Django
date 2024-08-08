from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def home_work(request):
    return HttpResponse("Hello Teacher!")


def main_page_view(request):
    return render(request, 'main_page.html')


def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', context={'post': post})