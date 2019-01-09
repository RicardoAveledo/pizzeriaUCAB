from django.db import models

"""Acá se define la base de datos que se diseñó para almacenar la data de los pedidos, tomando en cuenta
las consultas que se debían mostrar en la sección de Administración.
Se decidió crear una tabla con tres campos: La orden completa de la factura, esto incluye todos los valores 
y los detalles de la orden. El precio total de cada factura, y la fecha en la que se registraron."""
# Create your models here.
class Orden(models.Model):
	orden_detalle = models.CharField(max_length=500)
	precio = models.FloatField(null=True, blank=True, default=None)
	fecha = models.CharField(max_length=500)
	
	def __str__(self):
		registro = self.orden_detalle + '###' + str(self.precio) + '###'+self.fecha
		return registro
