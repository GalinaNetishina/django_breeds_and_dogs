from .models import Dog
from .serializers import DogSerializer
from rest_framework import generics


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.prefetch_related("breed").all()
    serializer_class = DogSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all().select_related()
    serializer_class = DogSerializer
