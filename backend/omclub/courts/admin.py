from django.contrib import admin
from .models import Court, Coach, TimeSlot, Reservation

	

admin.site.register(Court)
admin.site.register(Coach)
admin.site.register(Reservation)
admin.site.register(TimeSlot)
