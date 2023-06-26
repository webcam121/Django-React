from django.db import models

from hospital.models import Hospital
# Create your models here.

class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
