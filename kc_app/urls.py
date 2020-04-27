from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kc_app-home'),
    path('about/', views.about, name='kc_app-about'),
    path('services/', views.cat_services, name="kc_app-cat_services"),
    path('menu/', views.menu, name="kc_app-menu"),
    path('blog/', views.blog, name="kc_app-blog"),
    path('contact_us/', views.contact_us, name="kc_app-contact"),
]
