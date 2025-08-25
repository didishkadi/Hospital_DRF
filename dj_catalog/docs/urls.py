from django.urls import path
from .views import MedicalCardList, CardNoteList

urlpatterns = [
    path('card/', MedicalCardList.as_view()),
    path('note/', CardNoteList.as_view()),
]