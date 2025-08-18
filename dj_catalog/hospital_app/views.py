from django.shortcuts import render
from .serializers import (
    DoctorSerializer, 
    PatientSerializer, 
    MedicalCardSerializer, 
    MeetingsSerializer, 
    CardNoteSerializer, 
    MeetingPatientSerializer,
    UserSerializer
)
from .models import Doctor, Patient, MedicalCard, Meetings, CardNote, MeetingPatient, User
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, CreateAPIView
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

class MedicalCardList(ListCreateAPIView):
    queryset = MedicalCard.objects.all()
    serializer_class = MedicalCardSerializer

class MeetingsList(ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer

class CardNoteList(ListCreateAPIView):
    queryset = CardNote.objects.all()
    serializer_class = CardNoteSerializer

class MeetingPatientList(ListCreateAPIView):
    queryset = MeetingPatient.objects.all()
    serializer_class = MeetingPatientSerializer

class MeetingPatientUpdate(UpdateAPIView):
    queryset = MeetingPatient.objects.all()
    serializer_class = MeetingPatientSerializer