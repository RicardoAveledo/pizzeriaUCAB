"""Posts views."""

# Django
from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Orden
import time;


def index(request):
	inicio = request.GET.get('inicio','1')
	localtime = time.asctime( time.localtime(time.time()) )
	ver = 1
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
