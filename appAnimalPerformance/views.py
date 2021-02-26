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

def IngresarRendimiento(request):
	#Variables de los formularios
	fr= RendimientoForm(request.POST or None, request.FILES or None)
	fp = ProductoForm(request.POST or None,request.FILES or None)
	flt=LoteAnimalForm(request.POST or None,request.FILES or None)
	fa=Animal(request.POST or None, request.FILES or None)
	#Declaración de variables de las clases
	r=Rendimiento()
	lt=LoteAnimal()
	p=Producto()
	a=Animal()
	if request.method == 'POST':
		if fp.is_valid() and fr.is_valid() and flt.is_valid() and fa.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosP= fp.cleaned_data
			datosR= fr.cleaned_data
			datosLt= flt.cleaned_data
			datosA= fa.cleaned_data
			#Para ingresar el producto con sus campos calculados en la tabla a la base
			p.nombreProducto=datosP.get("nombreProducto")
			p.peso_producto=datosP.get("peso_producto")
			p.utilidad_producto=datosP.get("utilidad_producto")
			p.precio_costo=datosP.get("precio_costo")
			p.porcentaje_peso=datosP.get("porcentaje_peso")
			p.total_costo_producto=datosP.get("total_costo_producto")
			p.total_venta_producto=datosP.get("total_venta_producto")
			p.margen_utilidad_producto=datosP.get("margen_utilidad_producto")
			#Para registrar el rendimiento animal.
			r.nombreProveedor=datosR.get("nombreProveedor")
			r.total_costo=datosR.get("total_costo")
			r.total_venta=datosR.get("total_venta")
			r.margen_utilidad=datosR.get("margen_utilidad")
			r.rendimiento_neto=datosR.get("rendimiento_neto")
			r.merma_deshidratacion=datosR.get("merma_deshidratacion")
			r.porcentaje_peso_neto=datosR.get("porcentaje_peso_neto")
			r.hora=datosR.get("hora")
			r.fecha=datosR.get("fecha")
			#Para registrar al lote animal en la base.
			lt.peso_lote=datosLt.get("peso_lote")
			#Para registrar a los animales que entran
			a.nombreAnimal=datosA.get("nombreAnimal")
			a.peso_animal=datosA.get("peso_animal")
			a.precio_costo=datosA.get("precio_costo")
			if r.save() != True and lt.save() != True and p.save() != True and a.save() != True:
				return redirect(IngresarRendimiento)
	context={
	'fr':fr,
	'fp':fp,
	'flt':flt,
	'fa':fa,
	'r':r,
	'lt':lt,
	'p':p,
	'a':a,
	}
	return render(request,"IngresarRendimiento.html",context)

