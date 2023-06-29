from datetime import datetime, date

from django.db import models

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento =  models.DateTimeField(default=datetime.now, blank=True)
    estado = models.IntegerField(default=1)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)






