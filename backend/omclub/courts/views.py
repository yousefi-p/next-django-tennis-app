from urllib import response
from rest_framework import viewsets
from .models import Court, Coach, TimeSlot, Reservation, AvailabilityRequest
from rest_framework.views import APIView

from rest_framework.response import Response
from .serializers import CourtSerializer, CoachSerializer, TimeSlotSerializer, ReservationSerializer, AvailabilityRequestSeralizer, CourtCountSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from datetime import datetime, timedelta



class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class CourtNumberView(APIView):
    def get(self, request):
        count = Court.objects.count()
        return Response({"count": count})


class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class CoachNumberView(APIView):
    def get(self, request):
        count = Coach.objects.count()
        return Response({"count": count })

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Reservation.objects.all()
        return Reservation.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AvailabilityRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AvailabilityRequestSeralizer
    permission_classes = [IsAdminUser]
    queryset = AvailabilityRequest.objects.filter(approved=False)
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        req = self.get_object()
        req.approved = True
        req.save()
        return Response({'status': 'approved'})
    

class GenerateTimeSlots(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, court_id):
        try:
            court = Court.objects.get(id=court_id)
        except Court.DoesNotExist:
            return Response({"error": "Court not found"}, status=404)

        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        interval = request.data.get("interval", 60)  # Default interval is 30 minutes

        if not start_time or not end_time:
            return Response({"error": "Start time and end time are required"}, status=400)

        try:
            start_time = datetime.strptime(start_time, "%H:%M")
            end_time = datetime.strptime(end_time, "%H:%M")
        except ValueError:
            return Response({"error": "Invalid time format. Use HH:MM"}, status=400)

        if start_time >= end_time:
            return Response({"error": "Start time must be before end time"}, status=400)

        # Generate time slots
        current_time = start_time
        time_slots = []
        while current_time < end_time:
            next_time = current_time + timedelta(minutes=interval)
            if next_time > end_time:
                break
            time_slots.append(TimeSlot(court=court, start_time=current_time.time(), end_time=next_time.time()))
            current_time = next_time

        # Save time slots to the database
        TimeSlot.objects.bulk_create(time_slots)

        return Response({"message": "Time slots generated successfully", "count": len(time_slots)})