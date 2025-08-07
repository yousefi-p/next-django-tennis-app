from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib import admin
from .models import SMSCode, User
from django.utils import timezone
import requests



class SMSCodeView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        code = SMSCode.generate_code()
        SMSCode.objects.create(phone_number=phone, code=code)

        # Simulate sending SMS (replace with actual SMS service)
        payload = {
            'username': 'your_username',
            'password': 'your_password',
            'to': phone,
            'from': 'your_line',
            'text': f'ام کلابی عزیز کد تایید شما: {code}'
        }

        # requests.post('https://rest.payamak-panel.com/api/SendSMS/Base', data=payload)

        print (f'Sending SMS to {phone}: {code}')
        return Response({'message': 'کد ارسال شد'})
    
class VerifyCodeView(APIView):
    def post(self, request):
        phone = request.data.get('phone_number')
        code = request.data.get('code')

        
        sms = SMSCode.objects.filter(phone_number=phone, code=code).last()
        if not sms or sms.is_expired():
            return Response({'error': 'کد اشتباه یا منقضی شده'}, status=400)

        user, _ = User.objects.get_or_create(phone_number=phone)
        user.set_password(code)  
        user.save()
        return Response({'message': 'می‌توانید با این کد وارد شوید.'}) 


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'phone_number': user.phone_number,
            'is_staff': user.is_staff,
            'is_manager': user.is_manager,
            'is_superuser': user.is_superuser,
            'id': user.id
        })
