from rest_framework import serializers

from .models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        exclude = ["breed"]

    breed_ = serializers.CharField(
        source="breed.name", default="Unknown", read_only=True
    )
