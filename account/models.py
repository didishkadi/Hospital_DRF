from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        patient = 'patient', 'Patient'
        doctor = 'doctor', 'Doctor'

    role = models.CharField(max_length=10, choices=Role.choices)


class AbstractUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateField()

    class Meta:
        abstract = True


class Doctor(AbstractUserProfile):

    class Speciality(models.TextChoices):
        THERAPIST = 'therapist', 'Therapist'
        SURGEON = 'surgeon', 'Surgeon'
        OCULIST = 'oculist', 'Oculist'
        PEDIATRIST = 'pediatrist', 'Pediatrist'
        GP = 'gp', 'GP'
        NEUROLOGIST = 'neurologist', 'Neurologist'

    specialist = models.CharField(max_length=32, choices=Speciality.choices)

    def __str__(self):
        return f'Doctor {self.user.first_name} {self.user.last_name}'


class Patient(AbstractUserProfile):
    address = models.CharField(max_length=32)

    def __str__(self):
        return f'Patient {self.user.first_name} {self.user.last_name}'
