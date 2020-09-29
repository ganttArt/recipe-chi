from django.views.generic import TemplateView
from groceries_app.models import Meal


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class RecipesView(TemplateView):
    template_name = 'recipes/recipes.html'

class MealChoiceView(TemplateView):
    template_name = 'grocery_planner/gp1-meal-choice.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal_list'] = Meal.objects.order_by('name')
        return context