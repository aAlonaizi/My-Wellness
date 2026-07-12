from django.shortcuts import get_object_or_404, redirect, render

from pages.forms import DailyLogForm, ExerciseForm, MealForm

from .models import DailyLog, Exercise, Meal

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


######## Meals #######

def meals(request):
    meals = Meal.objects.all()
    return render(request, "meals/meals.html", {"meals": meals})

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

    return render(request, "meals/log-meal.html", {"meal_form": meal_form})

def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    return render(request, "meals/meal_detail.html", {"meal": meal})

def meal_update(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)

    if request.method == "POST":
        meal_form = MealForm(request.POST, instance=meal)
        if meal_form.is_valid():
            meal_form.save()
            return redirect("meal_detail", meal_id=meal.id)
    else:
        meal_form = MealForm(instance=meal)

    return render(request, "meals/meal_update.html", {"meal_form": meal_form})

def meal_delete(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)

    if request.method == "POST":
        meal.delete()
        return redirect("meals")

    return render(request, "meals/meal_confirm_delete.html", {"meal": meal})


####### Excersises ########

def exercises(request):
    exercises = Exercise.objects.all()
    return render(request, "exercises/exercises.html", {"exercises": exercises})

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
        return render(request, "exercises/log-exercise.html", {"exercise_form": exercise_form})

def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    return render(request, "exercises/exercise_detail.html", {"exercise": exercise})

def exercise_update(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)

    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, instance=exercise)
        if exercise_form.is_valid():
            exercise_form.save()
            return redirect("exercise_detail", exercise_id=exercise.id)
    else:
        exercise_form = ExerciseForm(instance=exercise)

    return render(request, "exercises/exercise_update.html", {"exercise_form": exercise_form})

def exercise_delete(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)

    if request.method == "POST":
        exercise.delete()
        return redirect("exercises")

    return render(request, "exercises/exercise_confirm_delete.html", {"exercise": exercise})

####### Daily-Logs ########

def daily_logs(request):
    daily_logs = DailyLog.objects.all()
    return render(request, "daily-logs/daily-logs.html", {"daily_logs": daily_logs})

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

    return render(request, "daily-logs/log-daily-log.html", {"daily_log_form": daily_log_form})

def daily_log_detail(request, daily_log_id):
    daily_log = get_object_or_404(DailyLog, id=daily_log_id)
    return render(request, "daily-logs/daily-log_detail.html", {"daily_log": daily_log})

def daily_log_update(request, daily_log_id):
    daily_log = get_object_or_404(DailyLog, id=daily_log_id)

    if request.method == "POST":
        daily_log_form = DailyLogForm(request.POST, instance=daily_log)
        if daily_log_form.is_valid():
            daily_log_form.save()
            return redirect("daily_log_detail", daily_log_id=daily_log.id)
    else:
        daily_log_form = DailyLogForm(instance=daily_log)

    return render(request, "daily-logs/daily-log_update.html", {"daily_log_form": daily_log_form})

def daily_log_delete(request, daily_log_id):
    daily_log = get_object_or_404(DailyLog, id=daily_log_id)

    if request.method == "POST":
        daily_log.delete()
        return redirect("daily_logs")

    return render(request, "daily-logs/daily-log_confirm_delete.html", {"daily_log": daily_log})