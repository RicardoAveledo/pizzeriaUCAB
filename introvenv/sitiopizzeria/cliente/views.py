from django.shortcuts import render
from django.http import HttpResponse
import time;


tamanos = [
    {
        'size': 'Pizza Grande',
        'precio': 580,
        'color':'btn-warning',
    },
    {
        'size': 'Pizza Mediana',
        'precio': 430,
        'color':'btn-primary',
    },
    {
        'size': 'Pizza Personal',
        'precio': 280,
        'color':'btn-success',
    }
]

ingredientes = [
    {
        'name': 'Jamón',
        'precio': 40,
        'color':'btn-warning',
    },
    {
        'name': 'Champiñones',
        'precio': 35,
        'color':'btn-primary',
    },
    {
        'name': 'Pimentón',
        'precio': 30,
        'color':'btn-success',
    },
    {
        'name': 'Doble Queso',
        'precio': 40,
        'color':'btn-dark',
    },
    {
        'name': 'Aceitunas',
        'precio': 57.5,
        'color':'btn-warning',
    },
    {
        'name': 'Pepperoni',
        'precio': 38.5,
        'color':'btn-primary',
    },
    {
        'name': 'Salchichón',
        'precio': 62.5,
        'color':'btn-success',
    }
]

def index(request):
	precio = request.GET.get('precio','0')
	acum = request.GET.get('acum','0')
	acum = float(acum) + float(precio)
	acumaux = request.GET.get('acumaux','0')
	acumaux = float(acumaux) + float(precio)
	agregar = request.GET.get('agregar','')
	order = request.GET.get('order','')
	inicio = request.GET.get('inicio','1')
	count = request.GET.get('count','0')
	listaorden = []
	detalle = []
	if (inicio=='1'):
		count = float(count) + float('1')
		mas = str(acumaux) +' Item '
		acumaux = 0
		order = order +mas+ agregar 
	elif (inicio=='2'):
		mas = ' - '
		order = order + agregar + mas
	elif (inicio=='3'):
		order = order + str(acumaux) 
		acumaux = 0
	localtime = time.asctime( time.localtime(time.time()) )
	ordenstr = order
	listaorden = ordenstr.split(' Item ')

	if (inicio=='1'):
		return render(request, 'clienteprincipal.html', {'localtime':localtime,'listaorden':listaorden,'tamanos': tamanos, 'precio':precio, 'acum':acum, 'acumaux':acumaux, 'agregar':agregar, 'order':order, 'count':count})
	elif (inicio=='2'):
		return render(request, 'ingredientes.html', {'localtime':localtime,'listaorden':listaorden,'ingredientes': ingredientes, 'precio':precio, 'acum':acum, 'acumaux':acumaux, 'agregar':agregar, 'order':order, 'count':count})
	elif (inicio=='3'):
		return render(request, 'procederpago.html', {'localtime':localtime,'listaorden':listaorden,'ingredientes': ingredientes, 'precio':precio, 'acum':acum, 'acumaux':acumaux, 'agregar':agregar, 'order':order, 'count':count})


