from django.shortcuts import render

from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal,Usuario
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,UsuarioForm
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers

# Create your views here.
def inicioAdmin(request):
	r=Rendimiento.objects.all()
	context={
	'r':r,
	}
	return render(request,"InicioAdmin.html",context)

def IngresarAnimal(request):
	fa=AnimalForm(request.POST or None, request.FILES or None)
	#Declaración de variables de las clases
	a=Animal.objects.get(idAnimal=request.GET['idAnimal'])
	fa.fields["nombreAnimal"].initial=a.nombreAnimal
	if request.method == 'POST':
		if fa.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosA= fa.cleaned_data
			#Para registrar a los animales que entran
			a.nombre_animal=datosA.get("nombre_animal")
			a.peso_animal=datosA.get("peso_animal")
			a.precio_costo=datosA.get("precio_costo")
			if a.save() != True:
				return redirect(IngresarLote)
	context={
	'fa':fa,
	}
	return render(request,"IngresarAnimal.html",context)

def IngresarLote(request):
	flt=LoteAnimalForm(request.POST or None, request.FILES or None)
	a=Animal.objects.get(idAnimal=request.GET['idAnimal'])
	flt.fields['idAnimal'].initial=a.idAnimal
	lt=LoteAnimal()
	#Declaración de variables de las clases
	if request.method == 'POST':
		if flt.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosLt= flt.cleaned_data
			#Para registrar a los animales que entran
			lt.idAnimal=datosLt.get("idAnimal")
			lt.peso_lote=datosLt.get("peso_lote")
			if lt.save() != True:
				return redirect(IngresarRendimiento)
	context={
	'flt':flt,
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
	'p':p,
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
			r.idProducto=datosR.get("idProducto")
			r.nombre_proveedor=datosR.get("nombre_proveedor")
			r.total_costo=datosR.get("total_costo")
			r.total_venta=datosR.get("total_venta")
			r.margen_utilidad=datosR.get("margen_utilidad")
			r.rendimiento_neto=datosR.get("rendimiento_neto")
			r.merma_deshidratacion=datosR.get("merma_deshidratacion")
			r.porcentaje_peso_neto=datosR.get("porcentaje_peso_neto")
			#r.hora=datosR.get("hora")
			#r.fecha=datosR.get("fecha")
			if r.save() != True:
				return redirect(ExportarRendimiento)
	context={
	'fr':fr,
	'r':r,	
	}
	return render(request,"IngresarRendimiento.html",context)

def ExportarRendimiento(request):
	
	return render(request,"ExportarRendimiento.html",context)
