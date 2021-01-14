from django.urls import path
from .views import HomeView, MealChoiceView, RecipeListView, RecipeDetailView, RecipeDetailSimpleView, IngredientPlanView, ShoppingListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('meal-choice', MealChoiceView.as_view(), name='meal-choice'),
    path('recipes/detail/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"),
    path('recipes/detail_simple/<int:pk>', RecipeDetailSimpleView.as_view(), name="recipe-detail-simple"), 
    path('recipes', RecipeListView.as_view(), name='recipes'),
    path('planner/meal-choice', MealChoiceView.as_view(), name='meal-choice'),
    path('planner/ingredient-choice', IngredientPlanView.as_view(), name='ingredient-plan'),
    path('planner/shopping-list', ShoppingListView.as_view(), name='shopping-list')
]