from django.db import models

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name