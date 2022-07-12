from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def reverse(request):
    return render(request, 'reverse.html')


def home(request):
    return render(request, 'home.html')
