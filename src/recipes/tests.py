from django.test import TestCase, Client
from .models import Recipe
from .forms import RecipesSearchForm
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class RecipeModelTest(TestCase):
    """Set up non-modified objects used by all test methods"""

    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,
            ingredients="Tea Leaves, Water, Sugar",
            author="Anonymous",
        )

    def test_recipe_name(self):
        """Test to ensure name is initialized correctly"""
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        """Test to ensure that the length of the recipe name field is a maximum of 100 characters"""
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the recipe name field and use it to query its max_length
        max_length = recipe._meta.get_field("name").max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 100)

    def test_cooking_time_is_float(self):
        """Test to ensure cooking_time is float"""
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertIs(type(cooking_time), float)

    def test_ingredients_max_length(self):
        """Test to ensure that the length of the ingredients field is a maximum of 350 characters"""
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 350)

    def test_difficulty_max_length(self):
        """test to ensure that the length of the difficulty field is a maximum of 12 characters"""
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("difficulty").max_length
        self.assertEqual(max_length, 12)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/recipes/1")

    def test_calculate_difficulty(self):
        """Test the calculate_difficulty method of Recipe model."""
        recipe = Recipe.objects.get(name="Tea")
        calculated_difficulty = recipe.calculate_difficulty()
        self.assertEqual(recipe.difficulty, calculated_difficulty)
        self.assertNotEqual(recipe.difficulty, "")
        self.assertIsNotNone(calculated_difficulty)


class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        Recipe.objects.create(
            name="Tea",
            ingredients="Tea Leaves, Water, Sugar",
        )
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_authorized_list_access(self):
        """Test accessing the list view as an authenticated user"""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("recipes:recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes_list.html")

    def test_authorized_details_access(self):
        """Test accessing the details view as an authenticated user"""
        self.client.login(username="testuser", password="testpassword")
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse("recipes:detail", args=[recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes_detail.html")

    def test_unauthorized_list_access(self):
        response = self.client.get(reverse("recipes:recipes"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/login/?next={reverse("recipes:recipes")}')

    def test_unauthorized_details_access(self):
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse("recipes:detail", args=[recipe.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f'/login/?next={reverse("recipes:detail", args=[recipe.id])}'
        )


class RecipeFormTest(TestCase):

    # Check if the form validates with correct data
    def test_valid_form(self):
        form_data = {
            "recipe_name": "",
            "ingredient": "",
            "chart_type": "#1",
        }
        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
