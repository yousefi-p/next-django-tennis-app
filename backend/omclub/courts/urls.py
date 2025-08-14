from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourtViewSet, CoachViewSet, TimeSlotViewSet, ReservationViewSet, AvailabilityRequestViewSet, GenerateTimeSlots, CourtNumberView, CoachNumberView, CourtTableInfoView

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
    path('courts-table-info/', CourtTableInfoView.as_view(), name='court-info'),
    path('coach-count/', CoachNumberView.as_view(), name='coach-count'),

]
