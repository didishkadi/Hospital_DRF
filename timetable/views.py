from .serializers import (
    MeetingsSerializer, MeetingParticipantSerializer
)
from .models import Meetings, MeetingParticipants
from rest_framework.generics import ListCreateAPIView, CreateAPIView, UpdateAPIView


class MeetingsList(ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer


class MeetingPatientList(CreateAPIView):
    queryset = MeetingParticipants.objects.all()
    serializer_class = MeetingParticipantSerializer


class MeetingPatientUpdate(UpdateAPIView):
    queryset = MeetingParticipants.objects.all()
    serializer_class = MeetingParticipantSerializer