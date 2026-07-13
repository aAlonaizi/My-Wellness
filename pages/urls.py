from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),

    path("/meals/log-meal", views.log_meal, name="log_meal"),
    path("meals/", views.meals, name="meals"),
    
    path("exercises/log-exercise", views.log_exercise, name="log_exercise"),
    path("exercises/exercises", views.exercises, name="exercises"),
    
    path("daily-logs/log-daily-log", views.log_daily_log, name="log_daily_log"),
    path("daily-logs/daily-logs", views.daily_logs, name="daily_logs"),  
]