from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class RecipesView(TemplateView):
    template_name = 'recipes/recipes.html'

class PlannerView(TemplateView):
    template_name = 'grocery_planner/planner.html'