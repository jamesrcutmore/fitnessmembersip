from django.shortcuts import render, redirect
from .models import Content, Product, Subscription
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
            return redirect('home')
        else:
            messages.error(request, f'Password must conatin 8 minimum characters')
            # return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'members/register.html', {'form': form})


def mealplans(request):
    mealplans = Product.objects.filter(categary="nutrition")
    print(mealplans)
    return render(request, 'members/mealplan.html', {'mealplans': mealplans})


def gymplans(request):
    gymplans = Product.objects.filter(categary="gym")
    return render(request, 'members/gymplan.html', {'gymplans': gymplans})
