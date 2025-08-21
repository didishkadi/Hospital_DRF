from django.urls import path
from .views import MeetingsList, MeetingPatientList, MeetingPatientUpdate
urlpatterns = [
    path('meeting/', MeetingsList.as_view()),
    path('pstatus/', MeetingPatientList.as_view()),
    path('pstatus/<int:pk>/', MeetingPatientUpdate.as_view()),
]