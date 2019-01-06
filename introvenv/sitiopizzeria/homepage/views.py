"""Posts views."""

# Django
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	order = request.GET.get('order','')
	inicio = request.GET.get('inicio','1')
	acum = request.GET.get('acum','0')
	ver = 1
	if (inicio=='1'):
		return render(request, 'home.html')
	elif (inicio=='2'):
		"""Acá agarramos todos los order y acum y los guardamos en la base de datos procesando 
		las cantidades, las pizzas, el dinero, cosas así"""
		ver = 2
		return render(request, 'home.html', {'ver':ver})
