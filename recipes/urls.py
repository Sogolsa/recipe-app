from django.urls import path
from .views import home
from .views import (
    RecipeListView,
    RecipeDetailView,
    create_recipe,
    update_recipe,
    delete_recipe,
    about_me,
)


app_name = "recipes"

# <pk> indicates the primary key of the object
urlpatterns = [
    path("", home, name="home"),
    path("aboutme/", about_me, name="about_me"),
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("create/", create_recipe, name="create_recipe"),
    path("update/<pk>", update_recipe, name="update_recipe"),
    path("delete/<pk>", delete_recipe, name="delete_recipe"),
]
