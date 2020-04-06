from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

reviews_d = [
    {
        'customer': 'Joshua',
        'r_title': 'Review 1',
        'content': 'Service is literally good.',
        'date': 'March 23, 2020'
    },

    {
        'customer': 'Sid',
        'r_title': 'Review 2',
        'content': 'Service is ok.',
        'date': 'January 05, 2020',
    }

]


def home(request):
    return render(request, 'kc_app/home.html', {'title': 'Home'})


def cat_services(request):
    return render(request, 'kc_app/services.html', {'title': 'Services'})


def order_online(request):
    return render(request, 'kc_app/order_online.html', {'title': 'Online Order'})


def reviews(request):
    contexts = {
        'reviews_d': reviews_d,
        'title': 'Reviews',
    }
    return render(request, 'kc_app/reviews.html', contexts)


def contact_us(request):
    return render(request, 'kc_app/contact.html', {'title': 'Contact us'})


def donate(request):
    return render(request, 'kc_app/donate.html', {'title': 'Donate'})


def about(request):
    return render(request, 'kc_app/about.html', {'title': 'About'})
