from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'members/home.html')

def about(request):
    return render(request,'members/about.html')

def services(request):
    return render(request,'members/services.html')

def login(request):
    return render(request,'members/login.html')

def register(request):
    return render(request,'members/register.html')