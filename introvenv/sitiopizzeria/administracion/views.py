from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Orden

# Create your views here.

"""Esta vista consta de una botonería con todas las opciones para las diferentes
consultas que podemos hacer a la base de datos. Se tiene una misma pantalla en la 
que se pasa como parámetros las ordenes que resultan de la consulta realizada por
medio del modelo que se estableció en Models de sitiopizza."""
def index(request):
	inicio = request.GET.get('inicio','0')
	if (inicio== '0'):
		return render(request, 'administracion.html', {})
	elif (inicio== '1'):
		ordenes = Orden.objects.values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '2'):
		ordenes = Orden.objects.order_by('-fecha').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '3'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Pizza Grande').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '4'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Pizza Mediana').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '5'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Pizza Personal').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '6'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Jamón').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '7'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Champiñones').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '8'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Pimentón').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '9'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Doble Queso').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '10'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Aceitunas').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '11'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Pepperoni').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '12'):
		ordenes = Orden.objects.filter(orden_detalle__contains='Salchichón').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
	elif (inicio== '13'):
		ordenes = Orden.objects.order_by('-precio').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})

"""Todas las llamadas a las consultas se realizan por medio de Orden.objects"""
