"""Posts views."""

# Django
from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Orden
import time;

"""En esta vista se trabaja el mismo esquema establecido para todas las pantallas de navegación:
Se pasa un parámetro en el url, el mismo es obtenido al comienzo de cada index, según el valor de
la variable inicio se realizan las operaciones pertinentes."""
def index(request):
	inicio = request.GET.get('inicio','1')
	"""Se obtiene la variable inicio de los parámetros pasados al url en la navegación"""
	localtime = time.asctime( time.localtime(time.time()) )
	ver = 1
	"""Cuando es 1, se procede a la navegación básica de inicio, con los dos botones de navegación
	Cliente y Administración. La navegación de estos y de todos los botones está definido dentro de las vistas"""
	if (inicio=='1'):
		return render(request, 'home.html')
	elif (inicio=='2'):
		"""Acá agarramos todos los order y acum y los guardamos en la base de datos procesando 
		las cantidades, las pizzas, el dinero, cosas así 
		Cuando es 2, significa que la navegación vino a partir de haber creado una pizza o una orden completa, por lo tanto todos 
		los parámetros estarán alojados dentro de los parámetros de navegación URL, por lo tanto, procedemos a guardar la data en la
		base de datos con el modelo Orden definido en Models.py dentro del paquete de homepage"""
		ver = 2
		order = request.GET.get('order','')
		acum = request.GET.get('acum','0')
		orden1 = Orden(orden_detalle = order, precio = float(acum), fecha = localtime)
		orden1.save()
		return render(request, 'home.html', {'order':order,'acum':acum,'localtime':localtime})

