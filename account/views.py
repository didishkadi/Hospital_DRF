from .serializers import (
    DoctorSerializer,
    PatientSerializer,
    UserSerializer
)
from .models import Doctor, Patient, User
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class PatientRegisterView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorRegisterView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
