from django.db import models
from django.shortcuts import reverse
from users.models import User
from django.conf import settings


# Create your models here.
class Recipe(models.Model):

    name = models.CharField(max_length=100)
    cooking_time = models.FloatField(help_text="in minutes", default=0)
    ingredients = models.CharField(max_length=350)
    difficulty = models.CharField(max_length=12, blank=True, default="")
    description = models.TextField(max_length=500, default="No description...")
    pic = models.ImageField(upload_to="recipes", default="no_picture.jpg")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    # author = models.CharField(max_length=120, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Takes pk as a primary key and generates a URL"""
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    @property
    def difficulty_level(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    def calculate_difficulty(self):
        """Calculate the difficulty of the recipe, based on cooking time and ingredients."""
        if not self.difficulty:
            num_ingredients = len(self.ingredients.split(", "))
            if self.cooking_time < 10:
                self.difficulty = "Easy" if num_ingredients < 4 else "Intermediate"
            else:
                self.difficulty = "Intermediate" if num_ingredients < 4 else "Hard"
        return self.difficulty

    def save(self, *args, **kwargs):
        if not self.difficulty:
            self.calculate_difficulty()
        super().save(*args, **kwargs)
