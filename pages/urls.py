from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("log-meal", views.log_meal, name="log_meal"),
    path("meals", views.meals, name="meals"),
    path("log-exercise", views.log_exercise, name="log_exercise"),
    path("exercises", views.exercises, name="exercises"),
    path("log-daily-log", views.log_daily_log, name="log_daily_log"),
    path("daily-logs", views.daily_logs, name="daily_logs"),  
]