from django.urls import path
from . import views


urlpatterns = [
    path("dogs/", views.DogList.as_view(), name="dogs"),
    path("dogs/<int:pk>/", views.DogDetail.as_view(), name="dog"),
]
