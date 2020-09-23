from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RecipesPageView(TemplateView):
    template_name = 'recipes/recipes.html'

class PlannerPageView(TemplateView):
    template_name = 'grocery_planner/planner.html'