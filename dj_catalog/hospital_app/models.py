from django.db import models
from django.contrib.postgres.indexes import GistIndex
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Role(models.TextChoices):
        patients = 'patient', 'Patient'
        doctors = 'doctor', 'Doctor'

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Doctor(User):
    __name__ = "Doctor"
    role = models.CharField(max_length = 10, choices = User.Role.choices, default = User.Role.doctors)

    class Speciality(models.TextChoices):
        THERAPIST = 'therapist', 'Therapist'
        SURGEON = 'surgeon', 'Surgeon'
        OCULIST = 'oculist', 'Oculist'
        PEDIATRIST = 'pediatrist', 'Pediatrist'
        GP = 'gp', 'GP'
        NEUROLOGIST = 'neurologist', 'Neurologist'

    specialist = models.CharField(max_length = 100, choices = Speciality.choices, default = Speciality.GP)

    def __str__(self):
        return f'Doctor {self.first_name} {self.last_name}'


class Patient(User):
    __name__ = "Doctor"
    role = models.CharField(max_length = 10, choices = User.Role.choices, default = User.Role.patients)
    
    def __str__(self):
        return f'Patient {self.first_name} {self.last_name}'


class MedicalCard(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 300)
    patient = models.OneToOneField(Patient, on_delete = models.CASCADE, unique = True)

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}: {self.title}'
    

class Meetings(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name='meetings_as_doctor')
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, related_name='meetings_as_patient')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    patients_status = models.ManyToManyField(Patient, through = 'MeetingPatient', related_name='patient_meetings_status')

    class Meta:
        indexes = [
            #  GistIndex(fields = ['start_time', 'end_time'], name = 'meetings_time_gistindex' )
        ]

    def __str__(self):
        return f'Meeting: Doctor {self.doctor.first_name} {self.doctor.last_name} with {self.patient.first_name} {self.patient.last_name}. {self.start_time} - {self.end_time}'
    

class CardNote(models.Model):
    medical_card = models.ForeignKey(MedicalCard, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.SET_NULL, null = True)
    date = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return f'Doctors {self.doctor} notes'
    

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