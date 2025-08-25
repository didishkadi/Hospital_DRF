from django.shortcuts import render
from .serializers import (
    MeetingsSerializer, 
    MeetingParticipantSerializer)
from .models import Meetings, MeetingParticipant
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView

class MeetingsList(ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer

class MeetingParticipantList(ListAPIView):
    queryset = MeetingParticipant.objects.all()
    serializer_class = MeetingParticipantSerializer

class MeetingParticipantUpdate(RetrieveUpdateAPIView):    
    queryset = MeetingParticipant.objects.all()
    serializer_class = MeetingParticipantSerializer