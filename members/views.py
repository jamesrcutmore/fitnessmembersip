from django.shortcuts import render
from .models import Content, Product, Subscription

# Create your views here.


def home(request):
    return render(request, 'members/home.html')


def about(request):
    return render(request, 'members/about.html')


def services(request):
    return render(request, 'members/services.html')


def products(request):
    return render(request, 'members/products.html')


def login(request):
    return render(request, 'members/login.html')


def register(request):
    return render(request, 'members/register.html')


def mealplans(request):
    mealplans = Product.objects.filter(categary="nutrition").select_related('content').all()
    print(mealplans)
    return render(request, 'members/mealplan.html', {'mealplans': mealplans})


def gymplans(request):
    return render(request, 'members/gymplan.html')
