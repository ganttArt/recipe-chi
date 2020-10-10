from django.urls import path
from .views import HomeView, AboutView, MealChoiceView, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('meal-choice', MealChoiceView.as_view(), name='meal-choice'),
    path('recipes/detail/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"), 
    path('recipes', RecipesView.as_view(), name='recipes'),
    path('planner/meal-choice', MealChoiceView.as_view(), name='meal-choice')
]