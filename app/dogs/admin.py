from django.contrib import admin


from .models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "age", "color", "breed"]
    ordering = ["name", "gender", "age"]
