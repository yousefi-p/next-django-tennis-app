from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, CoachViewSet, TimeSlotViewSet, ReservationViewSet, AvailabilityRequestViewSet, GenerateTimeSlots, CourtNumberView, CoachNumberView

router = DefaultRouter()
router.register(r'courts', CourtViewSet)
router.register(r'coaches', CoachViewSet)
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'availability-request', AvailabilityRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courts/<int:court_id>/generate-slots/', GenerateTimeSlots.as_view(), name='generate-slots'),
    path('court-count/', CourtNumberView.as_view(), name='court-count'),
    path('coach-count/', CoachNumberView.as_view(), name='coach-count'),

]
