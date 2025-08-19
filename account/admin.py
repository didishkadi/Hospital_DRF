from django.contrib import admin
from .models import (
    Doctor,
    Patient,
    User
)

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
