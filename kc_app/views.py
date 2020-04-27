from django.shortcuts import render
from django.http import HttpResponse
from kc_app.models import Review

# Create your views here.


def home(request):
    return render(request, 'kc_app/home.html', {'title': 'Home'})


def cat_services(request):
    return render(request, 'kc_app/services.html', {'title': 'Services'})


def menu(request):
    return render(request, 'kc_app/menu.html', {'title': 'Menu'})


def blog(request):
    contexts = {
        'reviews_d': Review.objects.all(),
        'title': 'Blog',
    }
    return render(request, 'kc_app/blog.html', contexts)


def contact_us(request):
    return render(request, 'kc_app/contact.html', {'title': 'Contact us'})


def about(request):
    return render(request, 'kc_app/about.html', {'title': 'About'})
