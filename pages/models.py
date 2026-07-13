from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
    
class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    meals = models.ManyToManyField(Meal, blank=True)

    def __str__(self):
        return str(self.date)