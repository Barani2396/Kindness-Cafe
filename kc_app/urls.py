from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kc_app-home'),
    path('about/', views.about, name='kc_app-about'),
    path('services/', views.cat_services, name="kc_app-cat_services"),
    path('order_online/', views.order_online, name="kc_app-order_online"),
    path('reviews/', views.reviews, name="kc_app-reviews"),
    path('contact_us/', views.contact_us, name="kc_app-contact"),
    path('donate/', views.donate, name="kc_app-donate"),
]
