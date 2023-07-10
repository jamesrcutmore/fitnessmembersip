from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('services/',views.services, name='services'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path("accounts/", include("allauth.urls")),
]
