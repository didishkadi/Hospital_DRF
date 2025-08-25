from rest_framework import serializers
from .models import Doctor, Patient, User, Department
from docs.serializers import MedicalCardSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class DoctorSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset = Department.objects.all(), allow_null = True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'first_name', 'last_name', 'age', 
                  'email', 'specialist', 'department', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['role'] = User.Role.DOCTOR
        password = validated_data.pop('password')
        doctor = Doctor(**validated_data)
        doctor.set_password(password)
        doctor.save()
        return doctor

class PatientSerializer(serializers.ModelSerializer):
    cards = MedicalCardSerializer(read_only = True, many = False, source='medicalcard')

    class Meta: 
        model = Patient
        fields = ['id', 'username', 'first_name', 'last_name', 'age', 
                  'email', 'address', 'password', 'cards']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['role'] = User.Role.PATIENT
        password = validated_data.pop('password')
        patient = Patient(**validated_data)
        patient.set_password(password)
        patient.save()
        return patient