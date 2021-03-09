from django.shortcuts import render

from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal,Usuario
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,UsuarioForm
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.utils import timezone
from django.shortcuts import redirect,render
# Create your views here.
def inicioAdmin(request):
	lt=LoteAnimal.objects.all()
	context={
	'lt':lt,
	}
	return render(request,"InicioAdmin.html",context)

def NumAnimales(request):
	lt=LoteAnimal.objects.all()
	context={
	'lt':lt,
	}
	return render(request,"NumAnimales.html",context)

def IngresarAnimal(request):
	fa=AnimalForm(request.POST or None, request.FILES or None)
	#a=Animal.objects.get(nombre_animal=request.GET['nombre_animal'])
	#fa.fields['nombre_animal'].initial='SSSSSSSS'
	A=5;
	a=Animal()
	if request.method == 'POST':
		if fa.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosA= fa.cleaned_data
			#Para registrar a los animales que entran
			a.nombre_animal=datosA.get("nombre_animal")
			a.peso_animal=datosA.get("peso_animal")
			if a.save() != True:
				return redirect(IngresarAnimal)
	context={
	'fa':fa,
	'A':A,
	}
	return render(request,"IngresarAnimal.html",context)

def IngresarLote(request, aux):
	#aux=5;
	animales=Animal.objects.all().order_by('-fecha')[:aux]
	flt=LoteAnimalForm(request.POST or None, request.FILES or None)
	lt=LoteAnimal()
	#Declaración de variables de las clases
	if request.method == 'POST':
		if flt.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosLt= flt.cleaned_data
			#Para registrar a los animales que entran
			lt.nombre_animal=datosLt.get("nombre_animal")
			lt.peso_lote=datosLt.get("peso_lote")
			lt.precio_costo=datosLt.get("precio_costo")
			if lt.save() != True:
				return redirect(inicioAdmin)
	context={
	'flt':flt,
	'a':animales,
	}
	return render(request,"IngresarLote.html",context)

def IngresarProducto(request):
	#Variables de los formularios
	fp = ProductoForm(request.POST or None,request.FILES or None)
	p=Producto()
	if request.method == 'POST':
		if fp.is_valid() :
			#Limpieza de la lista que guarda el formulario
			datosP= fp.cleaned_data
			#Para ingresar el producto con sus campos calculados en la tabla a la base
			p.nombre_producto=datosP.get("nombre_producto")
			p.peso_producto=datosP.get("peso_producto")
			p.utilidad_producto=datosP.get("utilidad_producto")
			p.precio_costo=datosP.get("precio_costo")
			p.porcentaje_peso=datosP.get("porcentaje_peso")
			p.total_costo_producto=datosP.get("total_costo_producto")
			p.total_venta_producto=datosP.get("total_venta_producto")
			p.margen_utilidad_producto=datosP.get("margen_utilidad_producto")
			
			if p.save() != True:
				return redirect(IngresarProducto)
	context={
	'fp':fp,
	}
	return render(request,"IngresarProducto.html",context)

def IngresarRendimiento(request):
	#Variables de los formularios
	fr= RendimientoForm(request.POST or None, request.FILES or None)
	#Declaración de variables de las clases
	r=Rendimiento()
	if request.method == 'POST':
		if fr.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosR= fr.cleaned_data
			#Para registrar el rendimiento animal.
			r.idLoteAnimal=datosR.get("idLoteAnimal")
			r.nombre_proveedor=datosR.get("nombre_proveedor")
			r.total_costo=datosR.get("total_costo")
			r.total_venta=datosR.get("total_venta")
			r.margen_utilidad=datosR.get("margen_utilidad")
			r.rendimiento_neto=datosR.get("rendimiento_neto")
			r.merma_deshidratacion=datosR.get("merma_deshidratacion")
			r.porcentaje_peso_neto=datosR.get("porcentaje_peso_neto")
			if r.save() != True:
				return redirect(ExportarRendimiento)
	context={
	'fr':fr,
	}
	return render(request,"IngresarRendimiento.html",context)

def ExportarRendimiento(request):
	
	return render(request,"ExportarRendimiento.html",context)
