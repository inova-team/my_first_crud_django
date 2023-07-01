from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento =  models.DateTimeField(default=datetime.now, blank=True)
    estado = models.IntegerField(default=1)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)

class InformacionPersonal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True)
    edad = models.IntegerField(null=True)
    profesion = models.CharField(max_length=100,null=True)
    pais = models.CharField(max_length=100,null=True)




