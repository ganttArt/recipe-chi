from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from groceries_app.models import Meal, IngredientQuantity, Measurement, Category, Ingredient
import operator

class HomeView(TemplateView):
    template_name = 'home.html'


class MealChoiceView(TemplateView):
    template_name = 'grocery_planner/gp1-meal-choice.html'

    def convert_to_tsp(self, measurement, quantity):
        if measurement == 'tbsp':
            quantity *= 3
        elif measurement == 'cup':
            quantity *= 48
        return quantity

    def check_tsp(self, quantity):
        measurement = 'tsp'
        if quantity >= 48:
            measurement = 'cup'
            quantity = quantity / 48
        elif quantity >= 3:
            measurement = 'tbsp'
            quantity = quantity / 3
        return measurement, quantity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal_list'] = Meal.objects.order_by('name')
        return context

    def post(self, request):
        all_ingredients = {}
        meals = request.POST
        for meal, batch_size in meals.items():
            if meal == 'csrfmiddlewaretoken':
                pass
            elif batch_size == '0':
                pass
            else:
                meal_id = Meal.objects.get(name=meal)
                ingredients = IngredientQuantity.objects.all().filter(meal_name=meal_id.id)
                for ingredient in ingredients:
                    # prep ingredient variables
                    quantity = ingredient.quantity * int(batch_size)
                    measurement = str(ingredient.measurement.measurement)
                    ingredient = str(ingredient.ingredient)
                    if measurement == 'cup' or measurement == 'tbsp':
                        quantity = self.convert_to_tsp(measurement, quantity)
                        measurement = 'tsp'
                    elif measurement == 'splash' or measurement == 'pinch':
                        measurement = 'to taste'

                    # add ingredient to all_ingredients
                    if ingredient not in all_ingredients:
                        all_ingredients[ingredient] = {measurement: quantity}
                    elif measurement in all_ingredients[ingredient]:
                        all_ingredients[ingredient][measurement] += quantity
                    else:
                        all_ingredients[ingredient][measurement] = quantity

        # normalize tsp, tbsp, cups
        for ingredient, measurements in all_ingredients.items():
            if 'tsp' in measurements:
                quantity = measurements['tsp']
                measurement, quantity = self.check_tsp(quantity)
                if measurement != 'tsp':
                    measurements[measurement] = quantity
                    del measurements['tsp']

        request.session['ingredients'] = all_ingredients
        return redirect('ingredient-plan')


class IngredientPlanView(TemplateView):
    def float_zero_to_int(self, number):
        if str(number).endswith('.0'):
            return str(number)[:-2]
        else:
            return number

    def get(self, request):
        all_ingredients = request.session.get('ingredients')
        measurements = Measurement.objects.all()
        categories = Category.objects.all()
        return render(
            request,
            'grocery_planner/gp2-ingredient-list.html',
            {'ingredients': all_ingredients,
             'all_measurements': measurements,
             'categories': categories}
        )

    def post(self, request):
        final_ingredients = {}
        post_ingredients = request.POST.copy()
        del post_ingredients['csrfmiddlewaretoken']
        
        # adding ingredients from the user added ingredients to final_ingredients
        if 'ingredient' in post_ingredients:
            added_items = zip(post_ingredients.pop('ingredient'),
                            post_ingredients.pop('category'),
                            post_ingredients.pop('quantity'),
                            post_ingredients.pop('measurement')
                            )
            name, category, quantity, measurement = 0, 1, 2, 3
            for ingredient in added_items:
                ingredient = {
                    'name': ingredient[name],
                    'quantity': self.float_zero_to_int(ingredient[quantity]),
                    'measurement': ingredient[measurement],
                    'category': ingredient[category]
                }
                if ingredient['category'] not in final_ingredients:
                    final_ingredients[ingredient['category']] = [ingredient]
                else:
                    final_ingredients[ingredient['category']].append(ingredient)

        # adding ingredients from the previously selected ingredients to final_ingredients
        for ing_name, value in post_ingredients.lists():
            db_ingredient = Ingredient.objects.get(ingredient=ing_name)
            for i in range(int(len(value) / 2)):
                final_ingredient = {
                    'name': ing_name,
                    'quantity': self.float_zero_to_int(value[i * 2]),
                    'measurement': value[(i * 2) + 1],
                    'category': db_ingredient.category.category
                }
                if final_ingredient['category'] not in final_ingredients:
                    final_ingredients[final_ingredient['category']] = [final_ingredient]
                else:
                    final_ingredients[final_ingredient['category']].append(final_ingredient)
        
        # sort ingredient lists
        for category, ingredients in final_ingredients.items():
            ingredients.sort(key=lambda i: i['name'])
        
        request.session['final_ingredients'] = final_ingredients
        return redirect('shopping-list')
        

class ShoppingListView(TemplateView):
    def get(self, request):
        final_ingredients = request.session.get('final_ingredients')
        return render(
            request,
            'grocery_planner/gp3-shopping-list.html',
            {'final_ingredients': final_ingredients}
        )

class RecipeListView(ListView):
    template_name = 'recipes/recipes_list.html'
    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal_list'] = Meal.objects.order_by('name')
        return context


class RecipeDetailView(DetailView):
    template_name = 'recipes/recipes_detail.html'
    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_list'] = IngredientQuantity.objects.filter(
            meal_name=context['meal'])
        return context


class RecipeDetailSimpleView(DetailView):
    template_name = 'recipes/recipes_detail_simple.html'
    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_list'] = IngredientQuantity.objects.filter(
            meal_name=context['meal'])
        return context
