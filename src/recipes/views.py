from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.
def home(request):
    """takes the request coming from the web application and returns
    the template available at recipes/home.html as a response."""
    return render(request, "recipes/recipes_home.html")


class RecipeListView(ListView):
    """Class based view"""

    model = Recipe  # Specify model
    template_name = "recipes/recipes_list.html"  # Specify template


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipes_detail.html"
