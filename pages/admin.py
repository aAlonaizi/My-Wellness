from django.contrib import admin
from .models import Meal, Category

# Register your models here.
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'date', 'category')
    
    def __str__(self):
        return self.name
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    def __str__(self):
        return self.name