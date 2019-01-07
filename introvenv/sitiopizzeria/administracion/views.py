from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Orden

# Create your views here.

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
	elif (inicio== '13'):
		ordenes = Orden.objects.order_by('-precio').values()
		return render(request, 'administracion.html', {'ordenes':ordenes})
