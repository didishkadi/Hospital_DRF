from django.shortcuts import render
from .serializers import (
    DoctorSerializer, 
    PatientSerializer, 
    UserSerializer,
    DepartmentSerializer
)
from .models import Doctor, Patient, User, Department
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class DepartmentList(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DoctorListView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientListView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer