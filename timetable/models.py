from django.db import models
from account.serializers import User


class Meetings(models.Model):
    host = models.ForeignKey(User, on_delete = models.CASCADE, related_name='host_meeting')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    participants = models.ManyToManyField(User, through='MeetingParticipants', related_name='meeting_participants')

    class Meta:
        indexes = [
            #  GistIndex(fields = ['start_time', 'end_time'], name = 'meetings_time_gistindex' )
        ]

    def __str__(self):
        return f'{self.host.first_name} {self.host.last_name}: {self.start_time} - {self.end_time}'


# TODO: implement CRUD
# class MedicalRecord(models.Model):
#     medical_card = models.ForeignKey(Patient, on_delete = models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete = models.SET_NULL, null = True)
#     date = models.DateTimeField(auto_now=True)
#     note = models.TextField()
#
#     def __str__(self):
#         return f'Doctors {self.doctor} notes'


class MeetingParticipants(models.Model):
    meeting = models.ForeignKey(Meetings, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)

    class Status(models.TextChoices):
            EXPECTATION = 'expectation', 'Expectation'
            REJECTED = 'rejected', 'Rejected'
            ACCEPTED = 'accepted', 'Accepted'

    status = models.CharField(max_length = 30, choices = Status.choices, default = Status.EXPECTATION)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['meeting', 'participant'],
                name='unique_meeting_participant'
            )
        ]

    def __str__(self):
        return f'{self.meeting.id}: {self.participant.first_name} {self.participant.last_name} - {self.status}'
