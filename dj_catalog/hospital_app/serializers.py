from rest_framework import serializers
from .models import Doctor, Patient, MedicalCard, Meetings, CardNote, MeetingPatient, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class PatientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']

class DoctorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']


class CardNoteSerializer(serializers.ModelSerializer):
    doctor_name = DoctorNameSerializer(read_only = True, source = 'doctor')

    class Meta:
        model = CardNote
        fields = ['id', 'doctor', 'doctor_name', 'medical_card', 'date', 'note']


class MedicalCardSerializer(serializers.ModelSerializer):
    notes = CardNoteSerializer(read_only = True, many = True, source = 'cardnote_set')
    patient_name = PatientNameSerializer(read_only = True, source = 'patient')

    class Meta:
        model = MedicalCard
        fields = ['id', 'title', 'content', 'patient', 'patient_name', 'notes']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'role', 'specialist']


class PatientSerializer(serializers.ModelSerializer):
    cards = MedicalCardSerializer(read_only = True, many = False, source='medicalcard')

    class Meta: 
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'role', 'cards']


class MeetingsSerializer(serializers.ModelSerializer):
    doctor_name = DoctorNameSerializer(read_only = True, source = 'doctor')
    patient_name = PatientNameSerializer(read_only = True, source = 'patient')

    class Meta:
        model = Meetings
        fields = ['id', 'doctor', 'doctor_name', 'patient', 'patient_name', 'start_time', 'end_time']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('Error. Time is incorrect')
        
        doctor = data['doctor']
        patient = data['patient']
        start_time = data['start_time']
        end_time = data['end_time']

        coinciding_meetings_doctor = Meetings.objects.filter(doctor = doctor, start_time__lt = end_time, end_time__gt = start_time)
        if coinciding_meetings_doctor.exists():
            raise serializers.ValidationError('At this time the doctor already has an appointment')
        
        coinciding_meetings_patient = Meetings.objects.filter(patient = patient, start_time__lt = end_time, end_time__gt = start_time)
        if coinciding_meetings_patient.exists():
            raise serializers.ValidationError('At this time the patient has another appointment')
        
        lunch_start = start_time.replace(hour = 12, minute = 0, second = 0, microsecond = 0)
        lunch_end = start_time.replace(hour = 13, minute = 0, second = 0, microsecond = 0)
        if start_time < lunch_end and end_time > lunch_start:
            raise serializers.ValidationError('At this time the doctor is on lunch break (12:00 - 13:00)')
        
        start_working = start_time.replace(hour = 9, minute = 30, second = 0, microsecond = 0)
        end_working = start_time.replace(hour = 20, minute = 0, second = 0, microsecond = 0)
        if start_time < start_working or end_time > end_working:
            raise serializers.ValidationError('Working hours from 9:00 to 20:00')

        return data
    
class MeetingPatientSerializer(serializers.ModelSerializer):
    patient_name = PatientNameSerializer(read_only = True, source = 'patient')

    class Meta:
        model = MeetingPatient
        fields =['id', 'meeting', 'patient', 'patient_name', 'status']

    def validate(self, data):
        meeting = data['meeting']
        patient = data['patient']
        if meeting and patient:
            if meeting.patient != patient:
                raise serializers.ValidationError('This patient does not have an appointment for this appointment')
        return data