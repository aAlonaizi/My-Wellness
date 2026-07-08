from django.shortcuts import redirect, render

from pages.forms import DailyLogForm, ExerciseForm, MealForm

from .models import DailyLog, Exercise, Meal

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def log_meal(request):
    if request.method == "POST":
        
        meal_form = MealForm(request.POST)

        if meal_form.is_valid():
            meal_form.save()
            action = request.POST.get("action")
            if action == "save_and_add_new":
                return redirect("log_meal")
            else:
                return redirect("meals")
        else:
            pass

    else:
        meal_form = MealForm()

    return render(request, "log-meal.html", {"meal_form": meal_form})

def meals(request):
    meals = Meal.objects.all()
    return render(request, "meals.html", {"meals": meals})

def exercises(request):
    exercises = Exercise.objects.all()
    return render(request, "exercises.html", {"exercises": exercises})

def log_exercise(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            exercise_form.save()
            action = request.POST.get("action")
            if action == "save_and_add_new":
                return redirect("log_exercise")
            else:
                return redirect("exercises")
        else:
            pass
    else:
        exercise_form = ExerciseForm()
        return render(request, "log-exercise.html", {"exercise_form": exercise_form})

def daily_logs(request):
    daily_logs = DailyLog.objects.all()
    return render(request, "daily-logs.html", {"daily_logs": daily_logs})

def log_daily_log(request):
    if request.method == "POST":
        
        daily_log_form = DailyLogForm(request.POST)

        if daily_log_form.is_valid():
            daily_log_form.save()

            action = request.POST.get("action")
            if action == "save_and_add_new":
                return redirect("log_daily_log")
            else:
                return redirect("daily_logs")
        else:
            pass

    else:
        daily_log_form = DailyLogForm()

    return render(request, "log-daily-log.html", {"daily_log_form": daily_log_form})