from django.db import models
from users.models import User
from django_jalali.db import models as jmodels


class Court(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام زمین')
    
    def __str__(self):
        return self.name

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='دستمزد ساعتی')

    def __str__(self):
        return self.user.phone_number

class TimeSlot(models.Model):
    objects = jmodels.jManager()
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='timeslots', verbose_name='زمین')
    start_time = jmodels.jDateTimeField(verbose_name='زمان شروع')
    end_time = jmodels.jDateTimeField(verbose_name='زمان پایان')
    is_available = models.BooleanField(default=True, verbose_name='در دسترس')

    def __str__(self):
        return f'{self.court.name} @ {self.start_time.strftime("%Y-%m-%d %H:%M")}'

class Reservation(models.Model):
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, verbose_name='سانس')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='مربی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return f'Reservation for {self.user.phone_number} at {self.timeslot}'
