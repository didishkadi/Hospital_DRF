from rest_framework import serializers
from .models import Meetings, MeetingPatient, Doctor, Patient
from account.serializers import DoctorSerializer, PatientSerializer


class MeetingPatientSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only = True)

    class Meta:
        model = MeetingPatient
        fields =['id', 'meeting', 'patient', 'status']

    def validate(self, data):
        meeting = data['meeting']
        patient = data['patient']
        if meeting and patient:
            if meeting.patient != patient:
                raise serializers.ValidationError('This patient does not have an appointment for this appointment')
        return data


class MeetingsSerializer(serializers.ModelSerializer):
    # participants = MeetingPatientSerializer()
    # doctor = DoctorSerializer()
    # patient = PatientSerializer()
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patients_status = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), many=True
    )

    class Meta:
        model = Meetings
        fields = ['id', 'doctor', 'patients_status', 'start_time', 'end_time']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('Error. Time is incorrect')
        
        doctor = data['doctor']
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
