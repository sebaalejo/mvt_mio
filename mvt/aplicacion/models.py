from django.db import models

class familiar(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    anio_nacimiento=models.DateField()
