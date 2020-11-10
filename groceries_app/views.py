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
        print(request.POST)
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
