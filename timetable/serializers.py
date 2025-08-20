from rest_framework import serializers
from .models import Meetings, MeetingParticipants, User


class MeetingParticipantSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(queryset=Meetings.objects.all())
    participants = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )

    class Meta:
        model = MeetingParticipants
        fields =['id', 'meeting', 'participants', 'status']


class MeetingsSerializer(serializers.ModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    participants = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )

    class Meta:
        model = Meetings
        fields = ['id', 'host', 'participants', 'start_time', 'end_time']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('Error. Time is incorrect')
        
        host = data['host']
        start_time = data['start_time']
        end_time = data['end_time']

        existing_meeting = Meetings.objects.filter(
            host=host,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if existing_meeting.exists():
            raise serializers.ValidationError('At this time the doctor already has an appointment')
        return data
