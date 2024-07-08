from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to="users", default="no_picture.jpg")
    bio = models.TextField(default="No bio...")

    def __str__(self):
        return str(self.name)
