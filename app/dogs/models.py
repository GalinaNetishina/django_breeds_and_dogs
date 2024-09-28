from breeds.models import Breed
from django.db import models


class Dog(models.Model):
    class Gender(models.Choices):
        M = "male"
        F = "female"

    name = models.CharField(max_length=32)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.SET_DEFAULT, default="Unknown")
    gender = models.CharField(choices=Gender, max_length=6, default="male")
    color = models.CharField(max_length=32)
    favorite_food = models.CharField(max_length=40, blank=True)
    favorite_toy = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.name}, {self.gender}, {self.age}, {self.breed.name}"
