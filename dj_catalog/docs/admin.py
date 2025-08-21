from django.contrib import admin
from .models import MedicalCard, CardNote

admin.site.register(MedicalCard)
admin.site.register(CardNote)