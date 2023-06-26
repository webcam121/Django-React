from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Hospital
from patient.models import Patient

# Create your views here.

def index(request):
    hospital_list = Hospital.objects.all()
    context = {
        'hospital_list': hospital_list
    }
    return render(request, 'hospital/index.html', context)

@login_required
def detail(request, hospital_id):
    try:
        patient_list = Patient.objects.filter(hospital_id = hospital_id)
        context = {
            'patient_list': patient_list,
            'hospital_id': hospital_id
        }
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return render(request, 'patient/index.html', context)
