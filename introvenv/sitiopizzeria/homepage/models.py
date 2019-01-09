from django.db import models

"""Acá se define la base de datos que se diseñó para almacenar la data de los pedidos, tomando en cuenta
las consultas que se debían mostrar en la sección de Administración."""
# Create your models here.
class Orden(models.Model):
	orden_detalle = models.CharField(max_length=500)
	precio = models.FloatField(null=True, blank=True, default=None)
	fecha = models.CharField(max_length=500)
	
	def __str__(self):
		registro = self.orden_detalle + '###' + str(self.precio) + '###'+self.fecha
		return registro
