from django.urls import path
from .views import HomePageView, AboutPageView, RecipesPageView, PlannerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('recipes', RecipesPageView.as_view(), name='recipes'),
    path('planner', PlannerPageView.as_view(), name='planner')
]