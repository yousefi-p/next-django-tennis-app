from rest_framework import serializers
from .models import Court, Coach, TimeSlot, Reservation
from khayyam import JalaliDatetime


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

def get(self, request):
    jalali_date = JalaliDatetime(request.user.date_joined).strftime('%Y/%m/%d')
    return Response({'joined': jalali_date})