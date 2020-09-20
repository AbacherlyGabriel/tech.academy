from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'website/index.html')


def login(request):
    return render(request, 'website/login.html')


def register(request):
    return render(request, 'website/register.html')