from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from pages.forms import DailyLogForm, ExerciseForm, MealForm

from .models import DailyLog, Exercise, Meal

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


######## Meals #######

@login_required
def meals(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, "meals/meals.html", {"meals": meals})

@login_required
def log_meal(request):
    if request.method == "POST":
        
        meal_form = MealForm(request.POST)

        if meal_form.is_valid():
            
            meal = meal_form.save(commit=False)
            meal.user = request.user
            meal.save()
            
            action = request.POST.get("action")
            if action == "save_and_add_new":
                return redirect("log_meal")
            else:
                return redirect("meals")
        else:
            pass

    else:
        meal_form = MealForm()

    return render(request, "meals/log-meal.html", {"meal_form": meal_form})

@login_required
def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)
    return render(request, "meals/meal_detail.html", {"meal": meal})

@login_required
def meal_update(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)

    if request.method == "POST":
        meal_form = MealForm(request.POST, instance=meal)
        if meal_form.is_valid():
            meal_form.save()
            return redirect("meal_detail", meal_id=meal.id)
    else:
        meal_form = MealForm(instance=meal)

    return render(request, "meals/meal_update.html", {"meal_form": meal_form})

@login_required
def meal_delete(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)

    if request.method == "POST":
        meal.delete()
        return redirect("meals")

    return render(request, "meals/meal_confirm_delete.html", {"meal": meal})


####### Excersises ########
@login_required
def exercises(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, "exercises/exercises.html", {"exercises": exercises})

@login_required
def log_exercise(request):
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            
            exercise = exercise_form.save(commit=False)
            exercise.user = request.user
            exercise.save()

            action = request.POST.get("action")
            if action == "save_and_add_new":
                return redirect("log_exercise")
            else:
                return redirect("exercises")
        else:
            pass
    else:
        exercise_form = ExerciseForm()
        return render(request, "exercises/log-exercise.html", {"exercise_form": exercise_form})

@login_required
def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user)
    return render(request, "exercises/exercise_detail.html", {"exercise": exercise})

@login_required
def exercise_update(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user)

    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, instance=exercise)
        if exercise_form.is_valid():
            exercise_form.save()
            return redirect("exercise_detail", exercise_id=exercise.id)
    else:
        exercise_form = ExerciseForm(instance=exercise)

    return render(request, "exercises/exercise_update.html", {"exercise_form": exercise_form})

@login_required
def exercise_delete(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user)

    if request.method == "POST":
        exercise.delete()
        return redirect("exercises")

    return render(request, "exercises/exercise_confirm_delete.html", {"exercise": exercise})

####### Daily-Logs ########
@login_required
def daily_logs(request):
    daily_logs = DailyLog.objects.filter(user=request.user)
    return render(request, "daily-logs/daily-logs.html", {"daily_logs": daily_logs})

@login_required
def log_daily_log(request):
    if request.method == "POST":
        
        daily_log_form = DailyLogForm(request.POST)

        if daily_log_form.is_valid():
            daily_log = daily_log_form.save(commit=False)
            daily_log.user = request.user
            daily_log.save()

            action = request.POST.get("action")
            if action == "save_and_add_new":
                return redirect("log_daily_log")
            else:
                return redirect("daily_logs")
        else:
            pass

    else:
        daily_log_form = DailyLogForm()

    return render(request, "daily-logs/log-daily-log.html", {"daily_log_form": daily_log_form})

@login_required
def daily_log_detail(request, daily_log_id):
    daily_log = get_object_or_404(DailyLog, id=daily_log_id, user=request.user)
    return render(request, "daily-logs/daily-log_detail.html", {"daily_log": daily_log})

@login_required
def daily_log_update(request, daily_log_id):
    daily_log = get_object_or_404(DailyLog, id=daily_log_id, user=request.user)

    if request.method == "POST":
        daily_log_form = DailyLogForm(request.POST, instance=daily_log)
        if daily_log_form.is_valid():
            daily_log_form.save()
            return redirect("daily_log_detail", daily_log_id=daily_log.id)
    else:
        daily_log_form = DailyLogForm(instance=daily_log)

    return render(request, "daily-logs/daily-log_update.html", {"daily_log_form": daily_log_form})

@login_required
def daily_log_delete(request, daily_log_id):
    daily_log = get_object_or_404(DailyLog, id=daily_log_id, user=request.user)

    if request.method == "POST":
        daily_log.delete()
        return redirect("daily_logs")

    return render(request, "daily-logs/daily-log_confirm_delete.html", {"daily_log": daily_log})