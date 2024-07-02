from django.test import TestCase
from .models import Recipe


# Create your tests here.
class RecipeModelTest(TestCase):
    """Set up non-modified objects used by all test methods"""

    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,
            ingredients="Tea Leaves, Water, Sugar",
            difficulty="Easy",
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
