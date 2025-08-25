from django.db import models
from account.models import User

class Meetings(models.Model):
    host = models.ForeignKey(User, on_delete = models.CASCADE, related_name='host_meeting')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    participants = models.ManyToManyField(User, through = 'MeetingParticipant', related_name='participant_meeting')

    class Meta:
        indexes = [
            #  GistIndex(fields = ['start_time', 'end_time'], name = 'meetings_time_gistindex' )
        ]

    def __str__(self):
        return f'Meeting: Doctor {self.host.first_name} {self.host.last_name}: {self.start_time} - {self.end_time}'
        

class MeetingParticipant(models.Model):
    meeting = models.ForeignKey(Meetings, on_delete = models.CASCADE)
    participant = models.ForeignKey(User, on_delete = models.CASCADE)

    class Status(models.TextChoices):
            EXPECTATION = 'expectation', 'Expectation'
            REJECTED = 'rejected', 'Rejected'
            ACCEPTED = 'accepted', 'Accepted'

    status = models.CharField(max_length = 30, choices = Status.choices, default = Status.EXPECTATION)

    class Meta:
        unique_together = ('meeting', 'participant')

    def __str__(self):
        return f'{self.participant.first_name} {self.participant.last_name} status: {self.status} in meeting {self.meeting.id}'