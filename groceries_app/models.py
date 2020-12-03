from django.db import models

class Meal(models.Model):
    instructions_boilerplate = "<li></li>"

    name = models.CharField(max_length=60, unique=True)
    recipe_category = models.CharField(max_length=40)
    times_eaten = models.PositiveIntegerField(default=0)
    cook_time_in_minutes = models.PositiveIntegerField(null=True, blank=True)
    portion_number = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="meal_images")
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True) # add default later
    date_added = models.DateField(auto_now_add=True)
    original_recipe_creator = models.CharField(max_length=40, null=True, blank=True)
    original_recipe_name = models.CharField(max_length=60, null=True, blank=True)
    recipe_link_one = models.URLField(null=True, blank=True)
    recipe_link_two = models.URLField(null=True, blank=True)
    affiliate_link = models.URLField(null=True, blank=True)
    other_link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.category


class Measurement(models.Model):
    measurement = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.measurement


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=60, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.ingredient


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField()
    measurement = models.ForeignKey(Measurement, on_delete=models.PROTECT)
    meal_name = models.ForeignKey(Meal, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.ingredient} for {self.meal_name}'
