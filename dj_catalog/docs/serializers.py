from rest_framework import serializers
from .models import CardNote, MedicalCard

class CardNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardNote
        fields = ['id', 'doctor', 'medical_card', 'date', 'note']


class MedicalCardSerializer(serializers.ModelSerializer):
    notes = CardNoteSerializer(read_only = True, many = True, source = 'cardnote_set')

    class Meta:
        model = MedicalCard
        fields = ['id', 'title', 'content', 'patient', 'notes']