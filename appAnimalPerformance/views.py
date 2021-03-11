from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal,Usuario
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,UsuarioForm, ProductoForm2
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.utils import timezone

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
	}
	return render(request,"IngresarAnimal.html",context)

def IngresarLote(request):

	a=Animal.objects.all().order_by('-fecha')[:2]
	flt=LoteAnimalForm(request.POST or None, request.FILES or None)
	lt=LoteAnimal()
	#flt.fields["peso_lote"].initial=aux
	#Declaración de variables de las clases
	if request.method == 'POST':
		if flt.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosLt= flt.cleaned_data
			#Para registrar a los animales que entran
			lt.nombre_proveedor=datosLt.get("nombre_proveedor")
			lt.peso_lote=datosLt.get("peso_lote")
			lt.precio_costo=datosLt.get("precio_costo")
			if lt.save() != True:
				return redirect(inicioAdmin)
	context={
	'flt':flt,
	'a':a,
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
			p.precio_venta=datosP.get("precio_venta")
			p.unidad=datosP.get("unidad")
			if p.save() != True:
				return redirect(IngresarProducto)
	context={
	'fp':fp,
	}
	return render(request,"IngresarProducto.html",context)

def IngresarRendimiento(request):
	#Variables de producto y recorrer la lista de productos
	fp1= ProductoForm2(request.POST or None,request.FILES or None)
	fp2= ProductoForm2(request.POST or None,request.FILES or None)
	fp3= ProductoForm2(request.POST or None,request.FILES or None)
	fp4= ProductoForm2(request.POST or None,request.FILES or None)
	fp5= ProductoForm2(request.POST or None,request.FILES or None)
	fp6= ProductoForm2(request.POST or None,request.FILES or None)
	fp7= ProductoForm2(request.POST or None,request.FILES or None)
	fp8= ProductoForm2(request.POST or None,request.FILES or None)
	fp9= ProductoForm2(request.POST or None,request.FILES or None)
	fp10= ProductoForm2(request.POST or None,request.FILES or None)
	fp11= ProductoForm2(request.POST or None,request.FILES or None)
	fp12= ProductoForm2(request.POST or None,request.FILES or None)
	fp13= ProductoForm2(request.POST or None,request.FILES or None)
	fp14= ProductoForm2(request.POST or None,request.FILES or None)
	fp15= ProductoForm2(request.POST or None,request.FILES or None)
	fp16= ProductoForm2(request.POST or None,request.FILES or None)
	fp17= ProductoForm2(request.POST or None,request.FILES or None)
	fp18= ProductoForm2(request.POST or None,request.FILES or None)
	fp19= ProductoForm2(request.POST or None,request.FILES or None)
	fp20= ProductoForm2(request.POST or None,request.FILES or None)
	fp21= ProductoForm2(request.POST or None,request.FILES or None)
	fp22= ProductoForm2(request.POST or None,request.FILES or None)
	fp23= ProductoForm2(request.POST or None,request.FILES or None)
	fp24= ProductoForm2(request.POST or None,request.FILES or None)
	fp25= ProductoForm2(request.POST or None,request.FILES or None)
	fp26= ProductoForm2(request.POST or None,request.FILES or None)

	P=Producto.objects.all()
	range(0,len(P))
	Prod1=Producto.objects.get(idProducto=P[0].idProducto)
	fp1.fields['precio_costo'].initial=Prod1.precio_costo
	Prod2=Producto.objects.get(idProducto=P[1].idProducto)
	fp2.fields['precio_costo'].initial=Prod2.precio_costo
	Prod3=Producto.objects.get(idProducto=P[2].idProducto)
	fp3.fields['precio_costo'].initial=Prod3.precio_costo
	Prod4=Producto.objects.get(idProducto=P[3].idProducto)
	fp4.fields['precio_costo'].initial=Prod4.precio_costo
	Prod5=Producto.objects.get(idProducto=P[4].idProducto)
	fp5.fields['precio_costo'].initial=Prod5.precio_costo
	Prod6=Producto.objects.get(idProducto=P[5].idProducto)
	fp6.fields['precio_costo'].initial=Prod6.precio_costo
	Prod7=Producto.objects.get(idProducto=P[6].idProducto)
	fp7.fields['precio_costo'].initial=Prod7.precio_costo
	Prod8=Producto.objects.get(idProducto=P[7].idProducto)
	fp8.fields['precio_costo'].initial=Prod8.precio_costo
	Prod9=Producto.objects.get(idProducto=P[8].idProducto)
	fp9.fields['precio_costo'].initial=Prod9.precio_costo
	Prod10=Producto.objects.get(idProducto=P[9].idProducto)
	fp10.fields['precio_costo'].initial=Prod10.precio_costo
	Prod11=Producto.objects.get(idProducto=P[10].idProducto)
	fp11.fields['precio_costo'].initial=Prod11.precio_costo
	Prod12=Producto.objects.get(idProducto=P[11].idProducto)
	fp12.fields['precio_costo'].initial=Prod12.precio_costo
	Prod13=Producto.objects.get(idProducto=P[12].idProducto)
	fp13.fields['precio_costo'].initial=Prod13.precio_costo
	Prod14=Producto.objects.get(idProducto=P[13].idProducto)
	fp14.fields['precio_costo'].initial=Prod14.precio_costo
	Prod15=Producto.objects.get(idProducto=P[14].idProducto)
	fp15.fields['precio_costo'].initial=Prod15.precio_costo
	Prod16=Producto.objects.get(idProducto=P[15].idProducto)
	fp16.fields['precio_costo'].initial=Prod16.precio_costo
	Prod17=Producto.objects.get(idProducto=P[16].idProducto)
	fp17.fields['precio_costo'].initial=Prod17.precio_costo
	Prod18=Producto.objects.get(idProducto=P[17].idProducto)
	fp18.fields['precio_costo'].initial=Prod18.precio_costo
	Prod19=Producto.objects.get(idProducto=P[18].idProducto)
	fp19.fields['precio_costo'].initial=Prod19.precio_costo
	Prod20=Producto.objects.get(idProducto=P[19].idProducto)
	fp20.fields['precio_costo'].initial=Prod20.precio_costo
	Prod21=Producto.objects.get(idProducto=P[20].idProducto)
	fp21.fields['precio_costo'].initial=Prod21.precio_costo
	Prod22=Producto.objects.get(idProducto=P[21].idProducto)
	fp22.fields['precio_costo'].initial=Prod22.precio_costo
	Prod23=Producto.objects.get(idProducto=P[22].idProducto)
	fp23.fields['precio_costo'].initial=Prod23.precio_costo
	Prod24=Producto.objects.get(idProducto=P[23].idProducto)
	fp24.fields['precio_costo'].initial=Prod24.precio_costo
	Prod25=Producto.objects.get(idProducto=P[24].idProducto)
	fp25.fields['precio_costo'].initial=Prod25.precio_costo
	Prod26=Producto.objects.get(idProducto=P[25].idProducto)
	fp26.fields['precio_costo'].initial=Prod26.precio_costo
	#Prod=Producto.objects.get(idProducto=)

	a=Animal.objects.all().order_by('-fecha')[:2]
	
	lt=LoteAnimal.objects.latest('fecha')
	CostoTotal=lt.precio_costo*lt.peso_lote
	fr= RendimientoForm(request.POST or None, request.FILES or None)
	#Declaración de variables de las clases
	r=Rendimiento()
	if request.method == 'POST':
		if fr.is_valid():
			#Limpieza de la lista que guarda el formulario
			datosR= fr.cleaned_data
			#Para registrar el rendimiento animal.
			r.total_costo=datosR.get("total_costo")
			r.total_venta=datosR.get("total_venta")
			r.margen_utilidad=datosR.get("margen_utilidad")
			r.rendimiento_neto=datosR.get("rendimiento_neto")
			r.merma_deshidratacion=datosR.get("merma_deshidratacion")
			r.porcentaje_peso_neto=datosR.get("porcentaje_peso_neto")
			if r.save() != True:
				return redirect(ExportarRendimiento)
	context={
	'fr':fr,'lt':lt,'ct':CostoTotal,
	'Prod1':Prod1,'fp1':fp1,'Prod2':Prod2,'fp2':fp2,'Prod3':Prod3,'fp3':fp3,'Prod4':Prod4,'fp4':fp4,'Prod5':Prod5,'fp5':fp5,
	'Prod6':Prod6,'fp6':fp6,'Prod7':Prod7,'fp7':fp7,'Prod8':Prod8,'fp8':fp8,'Prod9':Prod9,'fp9':fp9,'Prod10':Prod10,'fp10':fp10,
	'Prod11':Prod11,'fp11':fp11,'Prod12':Prod12,'fp12':fp12,'Prod13':Prod13,'fp13':fp13,'Prod14':Prod14,'fp14':fp14,
	'Prod15':Prod15,'fp15':fp15,'Prod16':Prod16,'fp16':fp16,'Prod17':Prod17,'fp17':fp17,'Prod18':Prod18,'fp18':fp18,
	'Prod19':Prod19,'fp19':fp19,'Prod20':Prod20,'fp20':fp20,'Prod21':Prod21,'fp21':fp21,'Prod22':Prod22,'fp22':fp22,
	'Prod23':Prod23,'fp23':fp23,'Prod24':Prod24,'fp24':fp24,'Prod25':Prod25,'fp25':fp25,'Prod26':Prod26,'fp26':fp26,
	}
	return render(request,"IngresarRendimiento.html",context)

def ExportarRendimiento(request):

	return render(request,"ExportarRendimiento.html",context)
