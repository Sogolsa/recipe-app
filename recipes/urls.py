from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

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
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]
