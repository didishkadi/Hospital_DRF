from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        PATIENT = 'patient', 'Patient'
        DOCTOR = 'doctor', 'Doctor'

    role = models.CharField(max_length = 10, choices = Role.choices)
    age = models.DateField(null = True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

class Department(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return f'Department: {self.name}'

class Doctor(User):
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True)
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
    address = models.CharField(max_length = 50)
    def __str__(self):
        return f'Patient {self.first_name} {self.last_name}'
