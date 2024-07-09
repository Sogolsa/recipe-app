from django.urls import path
from .views import home
from .views import RecipeListView, RecipeDetailView


app_name = "recipes"

# <pk> indicates the primary key of the object
urlpatterns = [
    path("", home),
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
]
