from django.db import models
from account.serializers import Doctor, Patient


class Meetings(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    patients_status = models.ManyToManyField(Patient, through='MeetingPatient')

    class Meta:
        indexes = [
            #  GistIndex(fields = ['start_time', 'end_time'], name = 'meetings_time_gistindex' )
        ]

    def __str__(self):
        return f'Meeting: Doctor {self.doctor.first_name} {self.doctor.last_name} with {self.patient.first_name} {self.patient.last_name}. {self.start_time} - {self.end_time}'


# TODO: implement CRUD
# class MedicalRecord(models.Model):
#     medical_card = models.ForeignKey(Patient, on_delete = models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete = models.SET_NULL, null = True)
#     date = models.DateTimeField(auto_now=True)
#     note = models.TextField()
#
#     def __str__(self):
#         return f'Doctors {self.doctor} notes'


class MeetingPatient(models.Model):
    meeting = models.ForeignKey(Meetings, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)

    class Status(models.TextChoices):
            EXPECTATION = 'expectation', 'Expectation'
            REJECTED = 'rejected', 'Rejected'
            ACCEPTED = 'accepted', 'Accepted'

    status = models.CharField(max_length = 30, choices = Status.choices, default = Status.EXPECTATION)

    class Meta:
        unique_together = ('meeting', 'patient')

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name} status: {self.status} in meeting {self.meeting.id}'