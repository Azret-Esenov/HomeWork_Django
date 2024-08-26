from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models import Post
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from users.models import Profile


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})
        form.cleaned_data.__delitem__('confirm_password')
        image = form.cleaned_data.pop('image')
        user = User.objects.create_user(
            **form.cleaned_data
        )
        Profile.objects.create(user=user, image=image)
        return redirect('/main_page/')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})
        user = authenticate(**form.cleaned_data)
        if user is None:
            form.add_error('username', f'Пользователь {form.cleaned_data.get('username')} не найден')
        login(request, user)
        return redirect('/main_page/')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/main_page/')


@login_required(login_url='login')
def profile_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'user/profile.html', context={'posts': posts})
