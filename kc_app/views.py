from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Kindess Cafe</h1><p>This is my first site, where i use django for backend and i really like this routing concept. Soon i will add more functionality to this site.</p>')

def about(request):
    return HttpResponse('<h1>About - Kindness Cafe</h1>')