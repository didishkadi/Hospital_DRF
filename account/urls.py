from django.urls import path
from .views import (
    DoctorRegisterView,
    PatientRegisterView,
    UserView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/doctor', DoctorRegisterView.as_view()),
    path('register/patient', PatientRegisterView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('users/', UserView.as_view())
]