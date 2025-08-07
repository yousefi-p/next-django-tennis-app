from django.contrib import admin

from .models import SMSCode, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_active', 'is_staff', 'is_manager', 'is_superuser')
    search_fields = ('phone_number',)
    list_filter = ('is_active', 'is_staff', 'is_manager', 'is_superuser')

@admin.register(SMSCode)
class SMSCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created_at')
    search_fields = ('phone_number', 'code')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)