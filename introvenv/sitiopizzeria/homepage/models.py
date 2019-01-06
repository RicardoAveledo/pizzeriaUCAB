from django.db import models

# Create your models here.
class Orden(models.Model):
	orden_detalle = models.CharField(max_length=500)
	precio = models.CharField(max_length=500)
	fecha = models.CharField(max_length=500)