from django.db import models


class Breed(models.Model):
    class Size(models.Choices):
        T = "Tiny"
        S = "Small"
        M = "Medium"
        L = "Large"

    Grade = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    name = models.CharField(max_length=50, unique=True)
    size = models.CharField(choices=Size, max_length=6)
    friendliness = models.IntegerField(choices=Grade, default=3)
    trainability = models.IntegerField(choices=Grade, default=3)
    shedding_amount = models.IntegerField(choices=Grade, default=3)
    exercise_need = models.IntegerField(choices=Grade, default=3)

    def __str__(self):
        return self.name
