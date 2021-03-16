from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,ProductoForm2
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.models import User

def inicioAdmin(request):
	if request.user.is_authenticated:
		return render(request, "InicioAdmin.html")
	else:
		return redirect('/AnimalPerformance/login')

def register(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			user=form.save()
			if user is not None:
				do_login(request, user)
				return redirect('/AnimalPerformance/')
			else:
				return redirect('/AnimalPerformance/login')
	return render(request, "registro.html", {'form': form})

def login(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username=u, password=p)
			if user is not None:
				do_login(request, user)
				return redirect('AnimalPerformance/')
	return render(request, "login.html", {'form': form})

def logout(request):
	do_logout(request)
	return redirect('/')

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
	if request.method == 'POST':
		if flt.is_valid():
			datosLt= flt.cleaned_data
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
	ProdAux=Producto()
	FormAux=ProductoForm2(request.POST or None)
	a=Animal.objects.all().order_by('-fecha')[:2]
	lt=LoteAnimal.objects.latest('fecha') #trae el último lote ingresado
	PesoLote=lt.peso_lote
	CostoTotal=lt.precio_costo*PesoLote #Total del costo del lote
	ListForms=[] #lista para guardar todos los formularios
	MargenUTR=0 #Margen de utilidad en todo el rendimiento
	MargenUTPKG=[] #Lista para guardar el margen $ de utilidad por KG en cada producto
	PCP=[] #Lista para guardar el precio de costo por producto
	TCP=[] #Lista que guarda el total de costo por producto segun el peso
	UPP=[] #Lista para guaradar las utilidades $ por producto
	RN=0 #Rendimiento neto
	TotalVP=0 #T
	MermaDES=0
	TotalCos=0 #Suma TOTAL del total del costo por producto
	TVP=[] #Lista que guarda total de la venta por producto
	PPP=[] #Lista que alamacena porcentaje de peso por producto en referecia al peso del lote
	# Creo la instancia de todos los productos de la base
	P=Producto.objects.all()
	#TODOS LOS CALCULOS DE LA APP SE ENCUENTRAN EN ESTA SECCIÓN
	#Calula el total de venta por producto y el porcentaje que equivale el peso de cada producto en referecia al peso del lote
	for x in range(0,len(P)):
		TVP.append(round((float(P[int(x)].peso_producto)*float(P[int(x)].precio_venta)),2))
		PPP.append(float(P[int(x)].peso_producto)/CostoTotal)
	#Total de venta de todos los productos
	for x in range(0,len(TVP)):
		TotalVP+=round(TVP[int(x)],2)
	#Calcula margen de utilidad del rendimiento
	if CostoTotal!=0 and TotalVP!=0:
		MargenUTR=round((((CostoTotal*100/TotalVP)-100)*(-1)),2)
	#calcula margen de utilidad por KG en cada producto
	for x in range(0,len(P)):
		MargenUTPKG.append(round(((float(P[int(x)].precio_venta)*MargenUTR)/100),2))
	#Calcula el precio de costo por producto
	range(0,len(MargenUTPKG))
	for x in range(0,len(P)):
		PCP.append(round(float(P[int(x)].precio_venta)-MargenUTPKG[x],2))
	#Calcula el costo total por producto segun el peso.
	range(0,len(PCP))
	for x in range(0,len(P)):
		TCP.append(round((float(P[int(x)].peso_producto)*PCP[x]),2))
	#Calcula la utilidad neta $ por producto y la suma de los totales en costo total por producto
	range(0,len(TVP)) #Preparamos las listas para poder iterar
	range(0,len(TCP))
	for x in range(0,len(P)):
		TCP.append(round(TVP[x]-TCP[x],2))
		TotalCos+=round(TCP[x],2)

	MermaDES=round((PesoLote-RN),2)

	for x in range(0,len(P)):
		RN=round(RN,2)+float(P[int(x)].peso_producto)
	#FIN DE LOS CALCULOS
	#ListForms.clear()
	for x in range(0,len(P)):
		ListForms.append(ProductoForm2(request.POST or None))
	range(0,len(PCP))#Preparamos las listas para poder recorrerlas
	range(0,len(TCP))#Preparamos las listas para poder recorrerlas
	#range(0,len(ListForms))
	for x in range(0,len(P)):
		ProdAux=Producto.objects.get(idProducto=P[x].idProducto)
		ListForms[x].fields['nombre_producto'].initial=P[x].nombre_producto
		ListForms[x].fields['precio_venta'].initial=P[x].precio_venta
		ListForms[x].fields['precio_costo'].initial=P[x].precio_costo
		ListForms[x].fields['utilidad_producto'].initial=round(TCP[x],2)
		ListForms[x].fields['peso_producto'].initial=P[x].peso_producto
		ListForms[x].fields['precio_costo'].initial=PCP[x]

	fr= RendimientoForm(request.POST or None)
	r=Rendimiento()
	fr.fields["total_costo"].initial=TotalCos
	fr.fields["total_venta"].initial=round(TotalVP,2)
	fr.fields["margen_utilidad"].initial=MargenUTR
	fr.fields["rendimiento_neto"].initial=RN
	fr.fields["merma_deshidratacion"].initial=round(PesoLote-RN,2)
	fr.fields["porcentaje_peso_neto"].initial=round((RN*100)/PesoLote,2)
	if request.method == 'POST':
		ListForms.clear()
		if fr.is_valid():
			datosR= fr.cleaned_data
			r.total_costo=datosR.get("total_costo")
			r.total_venta=datosR.get("total_venta")
			r.margen_utilidad=datosR.get("margen_utilidad")
			r.rendimiento_neto=datosR.get("rendimiento_neto")
			r.merma_deshidratacion=datosR.get("merma_deshidratacion")
			r.porcentaje_peso_neto=datosR.get("porcentaje_peso_neto")
			if r.save() != True:
				return redirect(IngresarRendimiento)
			else:
				return redirect('AnimalPerformance/listarR')
	context={
	'fr':fr,'lt':lt,'ct':CostoTotal,'LF':ListForms,
	'P':P,'RN':RN,'ct2':TotalCos,'MD':MermaDES,'ProdAux':ProdAux,
	'FormAux':FormAux,
	}
	return render(request,"IngresarRendimiento.html",context)


def ExportarRendimiento(request):

	return render(request,"ExportarRendimiento.html",context)
#LISTAR ENTIDADES########################################################################
def ListarAnimales(request):
	if request.user.is_authenticated:
		a= Animal.objects.all()
		context={'a':a,}
		return render(request,"listarAnimales.html",context)
	else:
		return redirect('/AnimalPerformance/login')

def ListarProductos(request):
	if request.user.is_authenticated:
		p= Producto.objects.all()
		context={
	    'p':p,
	    }
		return render(request,"listarProductos.html",context)
	else:
		return redirect('/AnimalPerformance/login')

def ListarLotes(request):
	if request.user.is_authenticated:
		lt= LoteAnimal.objects.all()
		context={
	    'lt':lt,
	    }
		return render(request,"listarLotes.html",context)
	else:
		return redirect('/AnimalPerformance/login')

def ListarRendimiento(request):
	if request.user.is_authenticated:
		r= Rendimiento.objects.all()
		context={
	    'r':r,
	    }
		return render(request,"listarRendimientos.html",context)
	else:
		return redirect('/AnimalPerformance/login')

#MODIFICAR ENTIDADES######################################################################
def modificarRendimiento(request):
	fr = RendimientoForm(request.POST or None,request.FILES or None)
	r = Rendimiento.objects.get(idRendimiento=request.GET['idRendimiento'])
	fr.fields["total_costo"].initial=r.total_costo
	fr.fields["total_venta"].initial=r.total_venta
	fr.fields["margen_utilidad"].initial=r.margen_utilidad
	fr.fields["rendimiento_neto"].initial=r.rendimiento_neto
	fr.fields["merma_deshidratacion"].initial=r.merma_deshidratacion
	fr.fields["porcentaje_peso_neto"].initial=r.porcentaje_peso_neto
	if request.method == 'POST':
		if fr.is_valid():
			datos= fr.cleaned_data
			r.total_costo=datos.get("total_costo")
			r.total_venta=datos.get("total_ventatotal_venta")
			r.margen_utilidad=datos.get("margen_utilidad")
			r.rendimiento_neto=datos.get("rendimiento_neto")
			r.merma_deshidratacion=datos.get("merma_deshidratacion")
			r.porcentaje_peso_neto=datos.get("porcentaje_peso_neto")
			if r.save() != True:
				return redirect(ListarRendimiento)
	context={
	'fr':fr,
    'r':r,
    }
	return render(request,"modificarRendimiento.html",context)
def modificarAnimal(request):
	fa= AnimalForm(request.POST or None,request.FILES or None)
	a = Animal.objects.get(idAnimal=request.GET['idAnimal'])
	fa.fields["nombre_animal"].initial=a.nombre_animal
	fa.fields["peso_animal"].initial=a.peso_animal
	if request.method == 'POST':
		if fa.is_valid():
			datos= fa.cleaned_data
			a.nombre_animal=datos.get("nombre_animal")
			a.peso_animal=datos.get("peso_animal")
			if a.save() != True:
				return redirect(ListarAnimales)
	context={
	'fa':fa,
    'a':a,
    }
	return render(request,"modificarAnimal.html",context)
def modificarProducto(request):
	fp= ProductoForm2(request.POST or None,request.FILES or None)
	p = Producto.objects.get(idProducto=request.GET['idProducto'])
	fp.fields["nombre_producto"].initial=p.nombre_producto
	fp.fields["peso_producto"].initial=p.peso_producto
	fp.fields["precio_costo"].initial=p.precio_costo
	fp.fields["precio_venta"].initial=p.precio_venta
	fp.fields["utilidad_producto"].initial=p.utilidad_producto
	fp.fields["porcentaje_peso_producto"].initial=p.porcentaje_peso_producto
	fp.fields["total_costo_producto"].initial=p.total_costo_producto
	fp.fields["total_venta_producto"].initial=p.total_venta_producto
	fp.fields["utilidad_producto_xKG"].initial=p.utilidad_producto_xKG
	fp.fields["unidad"].initial=p.unidad
	if request.method == 'POST':
		if fp.is_valid():
			datos= fp.cleaned_data
			p.nombre_producto=datos.get("nombre_producto")
			p.peso_producto=datos.get("peso_producto")
			p.precio_costo=datos.get("precio_costo")
			p.precio_venta=datos.get("precio_venta")
			p.utilidad_producto=datos.get("utilidad_producto")
			p.porcentaje_peso_producto=datos.get("porcentaje_peso_producto")
			p.total_costo_producto=datos.get("total_costo_producto")
			p.total_venta_producto=datos.get("total_venta_producto")
			p.utilidad_producto_xKG=datos.get("utilidad_producto_xKG")
			p.unidad=datos.get("unidad")
			if p.save() != True:
				return redirect(ListarProductos)
	context={
	'fp':fp,
    'p':p,
    }
	return render(request,"modificarProducto.html",context)
def modificarLote(request):
	flt= LoteAnimalForm(request.POST or None,request.FILES or None)
	lt = LoteAnimal.objects.get(idLoteAnimal=request.GET['idLoteAnimal'])
	flt.fields["peso_lote"].initial=lt.peso_lote
	flt.fields["precio_costo"].initial=lt.precio_costo
	flt.fields["nombre_proveedor"].initial=lt.nombre_proveedor
	if request.method == 'POST':
		if flt.is_valid():
			datos= flt.cleaned_data
			lt.peso_lote=datos.get("peso_lote")
			lt.precio_costo=datos.get("precio_costo")
			lt.nombre_proveedor=datos.get("nombre_proveedor")
			if lt.save() != True:
				return redirect(ListarLotes)
	context={
	'flt':flt,
    'lt':lt,
    }
	return render(request,"modificarLote.html",context)
