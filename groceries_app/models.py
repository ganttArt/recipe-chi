from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=60, unique=True)
    times_eaten = models.IntegerField()
    
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.ingredient


class Measurement(models.Model):
    measurement = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.measurement


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    measurement = models.ForeignKey(Measurement, on_delete=models.PROTECT)
    meal_name = models.ForeignKey(Meal, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ingredient} for {self.meal_name}'
