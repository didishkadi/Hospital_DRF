from django.urls import path
from .views import DoctorListView, PatientListView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('doctor/', DoctorListView.as_view()),
    path('patient/', PatientListView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('users/', UserView.as_view())
]