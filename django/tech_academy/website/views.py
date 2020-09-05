from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>tech.academy</h1>')


def login(request):
    return HttpResponse('<h1>login</h1>')