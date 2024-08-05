from django.shortcuts import render
from django.http import HttpResponse


def home_work(request):
    return HttpResponse("Hello Teacher!")


def main_page_view(request):
    return render(request, 'main_page.html')
