from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from breeds.models import Breed
from .models import Dog
from .serializers import DogSerializer


class DogsAPITestCase(APITestCase):
    def test_get_list(self):
        breed = Breed.objects.create(
            name='tests',
            size='S',
            friendliness=1,
            trainability=1,
            shedding_amount=3,
            exercise_need=5)
        dogs = [
            Dog.objects.create(name='dog1', breed=breed, age=1, gender='F', color='red'),
            Dog.objects.create(name='dog2', breed=breed, age=1, gender='M', color='black-white')
            ]
        url = reverse('dogs')
        response = self.client.get(url)
        serialized_data = DogSerializer(dogs, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(dogs), len(response.data))
        self.assertEqual(serialized_data, response.data)
