from django.shortcuts import render
from .serializers import (
    MedicalCardSerializer, 
    CardNoteSerializer
)
from .models import MedicalCard, CardNote
from rest_framework.generics import ListCreateAPIView

class MedicalCardList(ListCreateAPIView):
    queryset = MedicalCard.objects.all()
    serializer_class = MedicalCardSerializer

class CardNoteList(ListCreateAPIView):
    queryset = CardNote.objects.all()
    serializer_class = CardNoteSerializer