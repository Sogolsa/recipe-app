from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Recipe(models.Model):
    difficulty_choices = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )

    name = models.CharField(max_length=100)
    cooking_time = models.FloatField(help_text="in minutes", default=0)
    ingredients = models.CharField(max_length=350)
    difficulty = models.CharField(
        max_length=12, choices=difficulty_choices, default="Easy"
    )
    description = models.TextField(max_length=500, default="No description...")
    pic = models.ImageField(upload_to="recipes", default="no_picture.jpg")
    author = models.CharField(max_length=120, default="anonymous")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Takes pk as a primary key and generates a URL"""
        return reverse("recipes:detail", kwargs={"pk": self.pk})
