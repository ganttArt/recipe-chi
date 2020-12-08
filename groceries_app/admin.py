from django.contrib import admin
from .models import Meal, Ingredient, Measurement, IngredientQuantity, Category

admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(IngredientQuantity)
admin.site.register(Category)
