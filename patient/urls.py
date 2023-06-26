from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:hospital_id>', views.add_patient, name='add_patient'),
    # path('create/', views.patientCreate, name='patientCreate')
]
