from django import forms
from django.forms import TextInput, Textarea, NumberInput
from .models import Recipe

CHART__CHOICES = (  # Specify choices as a tuple
    ("#1", "Bar chart"),  # when user selects "Bar chart", it is stored as "#1"
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)


# Define Class based form imported from Django forms
class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Type a recipe or ingredient"}),
    )
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)


class CreateRecipeForm(forms.ModelForm):
    """Creating form for Recipe management"""

    class Meta:
        model = Recipe
        fields = ["name", "cooking_time", "ingredients", "description", "pic"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "cooking_time": NumberInput(attrs={"class": "form-control"}),
            "ingredients": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }
