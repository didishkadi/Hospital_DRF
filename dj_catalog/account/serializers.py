from rest_framework import serializers
from .models import Doctor, Patient, User
from docs.serializers import MedicalCardSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'role', 'specialist']

class PatientSerializer(serializers.ModelSerializer):
    cards = MedicalCardSerializer(read_only = True, many = False, source='medicalcard')

    class Meta: 
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'role']
