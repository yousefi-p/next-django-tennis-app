from rest_framework import serializers
from .models import Court, Coach, TimeSlot, Reservation, AvailabilityRequest
from django_jalali.serializers.serializerfield import JDateField, JDateTimeField


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'

class CourtCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()

class CoachSerializer(serializers.ModelSerializer):
    date = JDateField()
    time = JDateTimeField()
    class Meta:
        model = Coach
        fields = '__all__'

class CoachCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()

    
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


class AvailabilityRequestSeralizer(serializers.ModelSerializer):
    class Meta:
        mddel = AvailabilityRequest
        fields = '__all__'