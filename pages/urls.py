from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),

    path("meals/log-meal", views.log_meal, name="log_meal"),
    path("meals/", views.meals, name="meals"),
    path("meals/<int:meal_id>/", views.meal_detail, name="meal_detail"),
    path("meals/<int:meal_id>/edit/", views.meal_update, name="meal_update"),
    path("meals/<int:meal_id>/delete/", views.meal_delete, name="meal_delete"),

    path("exercises/log-exercise", views.log_exercise, name="log_exercise"),
    path("exercises/", views.exercises, name="exercises"),
    path("exercises/<int:exercise_id>/", views.exercise_detail, name="exercise_detail"),
    path("exercises/<int:exercise_id>/edit/", views.exercise_update, name="exercise_update"),
    path("exercises/<int:exercise_id>/delete/", views.exercise_delete, name="exercise_delete"),

    path("daily-logs/log-daily-log", views.log_daily_log, name="log_daily_log"),
    path("daily-logs/", views.daily_logs, name="daily_logs"),  
    path("daily-logs/<int:daily_log_id>/", views.daily_log_detail, name="daily_log_detail"),
    path("daily-logs/<int:daily_log_id>/edit/", views.daily_log_update, name="daily_log_update"),
    path("daily-logs/<int:daily_log_id>/delete/", views.daily_log_delete, name="daily_log_delete"),
]