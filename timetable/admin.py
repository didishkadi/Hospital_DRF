from django.contrib import admin
from .models import (
    Meetings,
    MeetingParticipants,
)

admin.site.register(Meetings)
admin.site.register(MeetingParticipants)