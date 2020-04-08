from django.shortcuts import render
from django.http import HttpResponse
from kc_app.models import Review

# Create your views here.


def home(request):
    return render(request, 'kc_app/home.html', {'title': 'Home'})


def cat_services(request):
    return render(request, 'kc_app/services.html', {'title': 'Services'})


def order_online(request):
    return render(request, 'kc_app/order_online.html', {'title': 'Online Order'})


def reviews(request):
    contexts = {
        'reviews_d': Review.objects.all(),
        'title': 'Reviews',
    }
    return render(request, 'kc_app/reviews.html', contexts)


def contact_us(request):
    return render(request, 'kc_app/contact.html', {'title': 'Contact us'})


def donate(request):
    return render(request, 'kc_app/donate.html', {'title': 'Donate'})


def about(request):
    return render(request, 'kc_app/about.html', {'title': 'About'})
