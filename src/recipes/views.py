from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin  # To protect CBV
from django.contrib.auth.decorators import login_required  # To protect FBV
from .forms import RecipesSearchForm
import pandas as pd
from django.db.models import Q


# Create your views here.
def home(request):
    """takes the request coming from the web application and returns
    the template available at recipes/recipes_home.html as a response."""
    return render(request, "recipes/recipes_home.html")


class RecipeListView(LoginRequiredMixin, ListView):
    """Class based view"""

    model = Recipe  # Specify model
    template_name = "recipes/recipes_list.html"  # Specify template
    context_object_name = "recipes"

    def get_queryset(self):
        # Initially, get all recipes
        return Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        """To show the form without submitting"""
        form = RecipesSearchForm()  # Create an empty search form
        recipes = self.get_queryset()  # Get all recipes
        return render(
            request,
            "recipes/recipes_list.html",
            {"form": form, "recipes": recipes},
        )  # Send the form and recipes to the template to be displayed

    def post(self, request, *args, **kwargs):
        """Is called when search form is submitted, handle form submission and filter recipes
        based on search term"""
        form = RecipesSearchForm(request.POST)  # Create a form with submitted data
        recipes = self.get_queryset()  # Get all recipes
        # chart = None
        no_results = False
        recipes_html = None

        if form.is_valid():
            """Check if the form is valid"""
            recipe_name = form.cleaned_data.get("recipe_name")  # Get the search term

            # Filter recipes based on the search term
            qs = Recipe.objects.filter(
                Q(name__icontains=recipe_name) | Q(ingredients__icontains=recipe_name)
            )
            if qs.exists():
                """If any recipes matches the search criteria"""
                recipes_df = pd.DataFrame(
                    qs.values()  # returns the list of recipes dictionaries
                )  # Converts the queryset to pandas dataframe
                recipes_html = recipes_df.to_html()
                recipes = qs

            else:
                no_results = True
                recipes_html = ""

        context = {
            "form": form,
            "recipes": recipes,
            "no_results": no_results,
            "recipes_html": recipes_html,
        }
        return render(request, "recipes/recipes_list.html", context)


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipes_detail.html"
