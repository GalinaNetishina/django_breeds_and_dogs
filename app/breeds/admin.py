from django.contrib import admin


from .models import Breed


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_need",
    ]
    ordering = [
        "name",
        "trainability",
        "shedding_amount",
        "friendliness",
        "exercise_need",
    ]
