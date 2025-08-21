from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        patients = 'patient', 'Patient'
        doctors = 'doctor', 'Doctor'

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Doctor(User):
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
    role = models.CharField(max_length = 10, choices = User.Role.choices, default = User.Role.patients)
    
    def __str__(self):
        return f'Patient {self.first_name} {self.last_name}'
