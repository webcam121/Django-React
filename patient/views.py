from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Patient
from hospital.models import Hospital
from patient.forms import AddPatientForm

# Create your views here.

@login_required
def add_patient(request, hospital_id):
    context_dict = {'form': None}
    form = AddPatientForm()

    if request.method == 'GET':
        context_dict['form'] = form
    elif request.method == 'POST':
        form = AddPatientForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            cleaned_data = form.cleaned_data
            patient_data = Patient.objects.create(first_name = cleaned_data['first_name'], last_name = cleaned_data['last_name'], phone_number = cleaned_data['phone_number'], hospital_id = hospital_id)
            patient_data.save()
            return redirect('detail',hospital_id=hospital_id)
        else:
            messages.error(request, 'Something went wrong.')

    return render(request, 'patient/add.html', context_dict)

