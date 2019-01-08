from django.db import models

# Create your models here.
class Orden(models.Model):
	orden_detalle = models.CharField(max_length=500)
	precio = models.FloatField(null=True, blank=True, default=None)
	fecha = models.CharField(max_length=500)
	
	def __str__(self):
		registro = self.orden_detalle + '###' + str(self.precio) + '###'+self.fecha
		return registro