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
		las cantidades, las pizzas, el dinero, cosas así"""
		ver = 2
		order = request.GET.get('order','')
		acum = request.GET.get('acum','0')
		orden1 = Orden(orden_detalle = order, precio = float(acum), fecha = localtime)
		orden1.save()
		return render(request, 'home.html', {'order':order,'acum':acum,'localtime':localtime})
