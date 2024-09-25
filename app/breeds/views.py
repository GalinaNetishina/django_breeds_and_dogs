from rest_framework import mixins, viewsets

from .models import Breed
from .serializers import BreedSerializer


class BreedList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer



class BreedDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


