from rest_framework import serializers
from .models import Meetings, MeetingParticipant
from account.models import User

class ParticipantsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class MeetingsSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    participants = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many = True)
    name = ParticipantsNameSerializer(read_only = True, source = 'participants', many = True)

    class Meta:
        model = Meetings
        fields = ['id', 'host', 'participants', 'name', 'start_time', 'end_time']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('Error. Time is incorrect')
        
        host = data['host']
        start_time = data['start_time']
        end_time = data['end_time']

        existing_meeting = Meetings.objects.filter(host=host, start_time__lt=end_time, end_time__gt=start_time)
        if existing_meeting.exists():
            raise serializers.ValidationError('At this time the doctor already has an appointment')

        coinciding_meetings_doctor = Meetings.objects.filter(host = host, start_time__lt = end_time, end_time__gt = start_time)
        if coinciding_meetings_doctor.exists():
            raise serializers.ValidationError('At this time the doctor already has an appointment')
             
        lunch_start = start_time.replace(hour = 12, minute = 0, second = 0, microsecond = 0)
        lunch_end = start_time.replace(hour = 13, minute = 0, second = 0, microsecond = 0)
        if start_time < lunch_end and end_time > lunch_start:
            raise serializers.ValidationError('At this time the doctor is on lunch break (12:00 - 13:00)')
        
        start_working = start_time.replace(hour = 9, minute = 30, second = 0, microsecond = 0)
        end_working = start_time.replace(hour = 20, minute = 0, second = 0, microsecond = 0)
        if start_time < start_working or end_time > end_working:
            raise serializers.ValidationError('Working hours from 9:00 to 20:00')
        return data
    
class MeetingParticipantSerializer(serializers.ModelSerializer):
    name = ParticipantsNameSerializer(read_only = True, source = 'participant')
    class Meta:
        model = MeetingParticipant
        fields =['id', 'meeting', 'participant', 'name', 'status']

    def validate(self, data):
        meeting = data.get('meeting')
        participant = data.get('participant')
        if meeting and participant:
            if not MeetingParticipant.objects.filter(meeting = meeting, participant = participant).exists():
                raise serializers.ValidationError('This participant does not have an appointment for this meeting')
        return data