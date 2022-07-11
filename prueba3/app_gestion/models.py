from email.policy import default
from pickle import TRUE
from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=15)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    edad = models.IntegerField()
    vacuna = models.CharField(max_length=50)
    fecha = models.CharField(max_length=20)


class Medico(models.Model):
    med_rut = models.CharField(primary_key=True, max_length=10)
    med_nombre = models.CharField(max_length=15)
    med_appaterno = models.CharField(max_length=50)
    med_apmaterno = models.CharField(max_length=50)
    med_fecha = models.CharField(max_length=20)