from django.db import models


class MyMeal(models.Model):
    name = models.CharField("Name of the Meal", max_length=50)
    recipe = models.TextField('Recipe of the Meal')
    image = models.ImageField(upload_to='images')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name



