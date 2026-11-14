from django.db import models

# Create your models here.
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()
    category = models.ForeignKey('ExerciseCategory', on_delete=models.RESTRICT, null=True, blank=True)



class ExerciseCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name