from django.urls import path
from .views import SMSCodeView, VerifyCodeView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('send-code/', SMSCodeView.as_view()),
    path('verify-code/', VerifyCodeView.as_view()),
    path('user-profile/', UserProfileView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
