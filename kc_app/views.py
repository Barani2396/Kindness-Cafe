from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    return render(request, 'kc_app/home.html', {'title': 'Home'})

def cat_services(request):
    return render(request, 'kc_app/cat_services.html', {'title': 'Services'})

def about(request):
    return render(request, 'kc_app/about.html', {'title': 'About'})