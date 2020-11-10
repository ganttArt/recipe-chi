from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.contrib import messages

from groceries_app.models import Meal, IngredientQuantity


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class MealChoiceView(TemplateView):
    template_name = 'grocery_planner/gp1-meal-choice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal_list'] = Meal.objects.order_by('name')
        return context

    def post(self, request):
        all_ingredients = {}
        meals = request.POST
        for meal, value in meals.items():
            if meal == 'csrfmiddlewaretoken':
                pass
            elif value == '0':
                pass
            else:
                meal_id = Meal.objects.get(name=meal)
                ingredients = IngredientQuantity.objects.all().filter(meal_name=meal_id.id)
                for ingredient in ingredients:
                    print(ingredient)
                    #will add ingredient to all_ingredients
                    #each ingredient will have a list of dictionaries or tuples that includes each ingredient entry.
        
        #will create a function to go through all_ingredients and make them the final 
                
        messages.info(request, "The grocery planning feature is still in development, thanks for trying 🙂")
        return render(request, 'grocery_planner/gp1-meal-choice.html')


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
        context['ingredient_list'] = IngredientQuantity.objects.filter(meal_name=context['meal'])
        return context
