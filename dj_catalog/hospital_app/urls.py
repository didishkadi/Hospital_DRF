from django.urls import path
from .views import DoctorListView, PatientListView, MedicalCardList, MeetingsList, CardNoteList, MeetingPatientList, MeetingPatientUpdate, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('doctor/', DoctorListView.as_view()),
    path('patient/', PatientListView.as_view()),
    path('card/', MedicalCardList.as_view()),
    path('meeting/', MeetingsList.as_view()),
    path('note/', CardNoteList.as_view()),
    path('pstatus/', MeetingPatientList.as_view()),
    path('pstatus/<int:pk>/', MeetingPatientUpdate.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('users/', UserView.as_view())
]