from django.db import models
from users.models import User
from django_jalali.db import models as jmodels
from django.conf import settings


class Court(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام زمین')
    
    class Meta:
        verbose_name = "زمین"
        verbose_name_plural = 'زمین‌ها'
        

    def __str__(self):
        return self.name
    
    def courts_count(self):
        return self.name.count()
    
    def court_table_field_info(self):
        return {
            "name": self.name
        }
    

        

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='دستمزد ساعتی')

    class Meta:
        verbose_name = 'مربی'
        verbose_name_plural = 'مربیان'

    def __str__(self):
        return self.user.phone_number

class TimeSlot(models.Model):
    court = models.ForeignKey('Court', on_delete=models.CASCADE, related_name='time_slots')
    start_time = models.TimeField(verbose_name='زمان شروع')
    end_time = models.TimeField(verbose_name='زمان پایان')

    class Meta:
        verbose_name = 'زمانبندی'
        verbose_name_plural = 'زمانبندی‌ها'

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


class AvailabilityRequest(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = jmodels.jDateField()
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    processed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'درخواست'
        verbose_name_plural = 'درخواست‌ها'


class Reservation(models.Model):
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, verbose_name='سانس')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='مربی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return f'Reservation for {self.user.phone_number} at {self.timeslot}'
