from django.db import models

# Create your models here.

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    description = models.TextField()
