from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, CoachViewSet, TimeSlotViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'coaches', CoachViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
