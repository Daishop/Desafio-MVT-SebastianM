from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    cumpleannios = models.DateField()
    parentezco = models.CharField(max_length=30)
