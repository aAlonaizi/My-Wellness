from django.contrib import admin
from .models import Exercise, ExerciseCategory

# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'date', 'category')

@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')