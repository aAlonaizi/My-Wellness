from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("log-meal", views.log_meal, name="log_meal"),
    path("meals", views.meals, name="meals"),
    path("exercises", views.exercises, name="exercises"),
    path("reports", views.reports, name="reports"),
]