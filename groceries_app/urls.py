from django.urls import path
from .views import HomeView, AboutView, MealChoiceView, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('meal-choice', MealChoiceView.as_view(), name='meal-choice'),
    path('recipes', RecipeListView.as_view()),
    path('recipes/detail/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"), 
]