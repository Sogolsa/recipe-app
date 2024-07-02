from django.db import models


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
    description = models.TextField()

    def __str__(self):
        return str(self.name)
