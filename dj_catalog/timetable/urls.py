from django.urls import path
from .views import MeetingsList, MeetingParticipantList, MeetingParticipantUpdate
urlpatterns = [
    path('meeting/', MeetingsList.as_view()),
    path('pstatus/', MeetingParticipantList.as_view()),
    path('pstatus/<int:pk>/', MeetingParticipantUpdate.as_view()),
]