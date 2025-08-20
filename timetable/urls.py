from django.urls import path
from .views import (
    MeetingsList,
)


urlpatterns = [
    path('meeting/', MeetingsList.as_view()),
]
