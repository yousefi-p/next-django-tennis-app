from django.contrib import admin
from .models import Court, Coach, TimeSlot, Reservation, AvailabilityRequest

	

admin.site.register(Reservation)
admin.site.register(TimeSlot)

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'hourly_rate')

@admin.register(AvailabilityRequest)
class AvailableRequestAdmin(admin.ModelAdmin):
    list_display = ('court', 'slot', 'date', 'requested_by', 'approved')
    search_fields = ('court', 'requested_by')
    list_filter = ('date','approved')