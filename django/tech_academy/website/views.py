from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'website/index.html')


def login(request):
    return HttpResponse('<h1>login</h1>')