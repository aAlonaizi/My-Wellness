from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def log_meal(request):
    return render(request, "log-meal.html")

def meals(request):
    return render(request, "meals.html")

def exercises(request):
    return render(request, "exercises.html")