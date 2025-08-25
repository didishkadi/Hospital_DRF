from django.db import models
from account.models import Patient, Doctor

class MedicalCard(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 300)
    patient = models.OneToOneField(Patient, on_delete = models.CASCADE, unique = True)

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}: {self.title}'
    
class CardNote(models.Model):
    medical_card = models.ForeignKey(MedicalCard, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.SET_NULL, null = True)
    date = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return f'Doctors {self.doctor} notes'