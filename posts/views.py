from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.forms import PostForm, SearchForm, PostUpdateForm, CommentForm
from posts.models import Post, Comment
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
import random


class TestView(View):
    def get(self, request):
        return HttpResponse(f'Hello word {random.randint(0, 100)}')


def home_work(request):
    if request.method == 'GET':
        return HttpResponse("Hello Teacher!")


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')


@login_required(login_url='login')
def posts_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        tags = request.GET.get('tags')
        orderings = request.GET.get('orderings')
        searchform = SearchForm(request.GET)
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tags:
            posts = posts.filter(tags__id__in=tags.split(','))
        if orderings:
            posts = posts.order_by(orderings)

        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]
        context = {'posts': posts, 'search_form': searchform, 'max_pages': range(1, max_pages + 1)}
        return render(request, 'posts/post_list.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


@login_required(login_url='login')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        comments = post.comments.all()
        comment_form = CommentForm()
        return render(request, 'posts/post_detail.html', context={'post': post, 'comment_form': comment_form, 'comments': comments})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(request, 'posts/post_detail.html', context={'post': post, 'comment_form': form})
        Comment.objects.create(text=form.cleaned_data.get('text'), post_id=post_id)
    return redirect('/posts/')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    lookup_url_kwarg = 'post_id'
    form_class = CommentForm


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


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostForm
    success_url = '/posts2/'


@login_required(login_url='login')
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostUpdateForm(instance=post)
        return render(request, 'posts/post_update.html', {'form': form})
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_update.html', {'form': form})
        form.save()
    return redirect('/profile/')
