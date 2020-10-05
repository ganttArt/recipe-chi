from django.urls import path
from .views import HomeView, AboutView, RecipesView, MealChoiceView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('recipes', RecipesView.as_view(), name='recipes'),
    path('planner/meal-choice', MealChoiceView.as_view(), name='meal-choice')
]