from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("submit/", views.submit, name="submit"),
	path('recipes/', views.RecipeList, name='recipes'),
	path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
]