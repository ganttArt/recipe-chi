from django.urls import path
from .views import HomeView, AboutView, MealChoiceView, RecipeListView, RecipeDetailView, IngredientPlanView, ShoppingListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('meal-choice', MealChoiceView.as_view(), name='meal-choice'),
    path('recipes/detail/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"), 
    path('recipes', RecipeListView.as_view(), name='recipes'),
    path('planner/meal-choice', MealChoiceView.as_view(), name='meal-choice'),
    path('planner/ingredient-choice', IngredientPlanView.as_view(), name='ingredient-plan'),
    path('planner/shopping-list', ShoppingListView.as_view(), name='shopping-list')
]