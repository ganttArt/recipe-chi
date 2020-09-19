from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=60, unique=True)
    times_eaten = models.PositiveIntegerField()
    photo = models.ImageField()
    cook_time = models.PositiveIntegerField()
    portion_number = models.PositiveIntegerField()
    original_recipe_link = models.URLField()
    other_link = models.URLField(blank=True)
    original_recipe_creator = models.CharField(max_length=40)
    original_recipe_name = models.CharField(max_length=60)
    recipe_category = models.CharField(max_length=40)
    description = models.TextField()
    instructions = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=60, unique=True)
    category = models.CharField(max_length=20) # potentially add choices later when I get a good understanding of what the choices are

    def __str__(self):
        return self.ingredient


class Measurement(models.Model):
    measurement = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.measurement


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    measurement = models.ForeignKey(Measurement, on_delete=models.PROTECT)
    meal_name = models.ForeignKey(Meal, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ingredient} for {self.meal_name}'
