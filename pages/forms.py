from django import forms
from .models import DailyLog, Exercise, Meal


class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ['date', 'notes', 'exercises', 'meals']
        
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'emoji']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['date', 'name', 'calories', 'category']