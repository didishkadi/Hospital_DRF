from django.shortcuts import render
from .serializers import (
    DoctorSerializer, 
    PatientSerializer, 
    UserSerializer
)
from .models import Doctor, Patient, User
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class Register(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        return 

class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class DoctorListView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientListView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer