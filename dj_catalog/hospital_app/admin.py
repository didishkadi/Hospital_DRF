from django.contrib import admin
from .models import Doctor, Patient, MedicalCard, Meetings, CardNote, MeetingPatient

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(MedicalCard)
admin.site.register(Meetings)
admin.site.register(CardNote)
admin.site.register(MeetingPatient)