from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kc_app-home'),
    path('about/', views.about, name='kc_app-about'),
    path('cat_services', views.cat_services, name="kc_app-cat_services"),
]