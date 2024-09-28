from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"breeds", views.BreedList, basename="breeds")
router.register("breeds", views.BreedDetail, basename="breed")
urlpatterns = router.urls
