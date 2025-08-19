from .serializers import (
    MeetingsSerializer,
    MeetingPatientSerializer,
)
from .models import Meetings, MeetingPatient
from rest_framework.generics import ListCreateAPIView, UpdateAPIView


class MeetingsList(ListCreateAPIView):
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer


class MeetingPatientList(ListCreateAPIView):
    queryset = MeetingPatient.objects.all()
    serializer_class = MeetingPatientSerializer


class MeetingPatientUpdate(UpdateAPIView):
    queryset = MeetingPatient.objects.all()
    serializer_class = MeetingPatientSerializer
