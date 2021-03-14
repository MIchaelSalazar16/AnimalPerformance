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


# Create your views here.
def welcome(request):
	if request.user.is_authenticated:
		return render(request, "welcome.html")
	else:
		return redirect('/login')


def register(request):
	form = UserCreationForm(request.POST or None, request.FILES or None)
	user=User()
	if request.method == "POST":
		if form.is_valid():
			#Limpieza de la lista que guarda el formulario
			datos= form.cleaned_data
			#Para registrar a los animales que entran
			user.username=datos.get("username")
			user.password=datos.get("password1")
			if user.save() != True:
				return redirect(register)
			else:
				# do_login(request, user)
				return redirect(login)

	return render(request, "registro.html", {'form': form})

def login(request):
	form = AuthenticationForm(request.POST or None, request.FILES or None)
	user=User()
	if request.method == "POST":
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username=u, password=p)
			if user is not None:
				do_login(request, user)
				return redirect(welcome)
	return render(request, "login.html", {'form': form})

def logout(request):
	# Finalizamos la sesión
	do_logout(request)
	return redirect('/')

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
	#Calula el rendimiento neto y el porcentaje que equivale el peso de cada producto en referecia al peso del lote
	for x in range(0,len(P)):
		RN=round(RN,2)+float(P[int(x)].peso_producto)
		TVP.append(round((float(P[int(x)].peso_producto)*float(P[int(x)].precio_venta)),2))
		PPP.append(float(P[int(x)].peso_producto)/CostoTotal)
	#Total de venta de todos los productos
	for x in range(0,len(TVP)):
		TotalVP+=round(TVP[int(x)],2)
	#Calcula margen de utilidad del rendimiento
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
	#FIN DE LOS CALCULOS
	# recorremos la lsita de productos para crear una lista alterna para alamacenar formualrios
	P1=Producto.objects.all()
	for x in range(0,len(P1)):
		ListForms.append(int(x))
	range(0,len(ListForms))
	# if request.method == 'GET':
	for x in range(0,len(P1)):
		ListForms[x]=ProductoForm2(request.POST or None,request.FILES or None)
		ListForms[x].fields['nombre_producto'].initial=P1[x].nombre_producto
		ListForms[x].fields['precio_venta'].initial=P1[x].precio_venta
		ListForms[x].fields['utilidad_producto'].initial=P1[x].utilidad_producto
		ListForms[x].fields['peso_producto'].initial=0
		ListForms[x].fields['precio_costo'].initial=0
	# elif request.method == 'GET':
	P2=Producto.objects.all()
	range(0,len(PCP))#Preparamos las listas para poder recorrerlas
	range(0,len(TCP))#Preparamos las listas para poder recorrerlas
	ListForms.clear()
	for x in range(0,len(P2)):
		ListForms.append(int(x))
	range(0,len(ListForms))
	for x in range(0,len(P2)):
		#Pasamos los precios de costo calculados al formulario de rendimiento
		ListForms[x]=ProductoForm2(request.POST or None,request.FILES or None)
		ListForms[x].fields['nombre_producto'].initial=P2[x].nombre_producto
		ListForms[x].fields['precio_venta'].initial=P2[x].precio_venta
		ListForms[x].fields['utilidad_producto'].initial=round(TCP[x],2)
		ListForms[x].fields['peso_producto'].initial=P2[x].peso_producto
		ListForms[x].fields['precio_costo'].initial=PCP[x]
			# FormAux=ProductoForm2(request.POST or None,request.FILES or None)
			# ProdAux=Producto.objects.get(idProducto=P[x].idProducto)
			# FormAux.fields['nombre_producto'].initial=ProdAux.nombre_producto
			# FormAux.fields['precio_venta'].initial=ProdAux.precio_venta
			# FormAux.fields['utilidad_producto'].initial=ProdAux.utilidad_producto
			# FormAux.fields['peso_producto'].initial=0
			# FormAux.fields['precio_costo'].initial=0
			# if FormAux.is_valid():
			# 	datosP= FormAux.cleaned_data
			# 	ProdAux.nombre_producto=datosP.get("nombre_producto")
			# 	ProdAux.precio_venta=datosP.get("precio_venta")
			# 	ProdAux.utilidad_producto=datosP.get("utilidad_producto")
			# 	ProdAux.peso_producto=datosP.get("peso_producto")
			# 	ProdAux.precio_costo=datosP.get("precio_costo")
			# 	if ProdAux.save() != True:
			# 		return redirect(IngresarRendimiento)
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
	'fr':fr,'lt':lt,'ct':CostoTotal,'ListForms':ListForms,
	'P':P,'RN':RN,'ct2':TotalCos,'MD':MermaDES
	}
	return render(request,"IngresarRendimiento.html",context)

def ExportarRendimiento(request):

	return render(request,"ExportarRendimiento.html",context)
