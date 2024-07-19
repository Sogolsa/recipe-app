from django import forms

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
