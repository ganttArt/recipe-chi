from django.urls import path
from .views import HomeView, AboutView, RecipesView, PlannerView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('recipes', RecipesView.as_view(), name='recipes'),
    path('planner', PlannerView.as_view(), name='planner')
]