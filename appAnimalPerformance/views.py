from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal,Usuario
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,UsuarioForm, ProductoForm2 , UsuarioLoginForm
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
	ListForms=[]
	# Creo la instancia de todos los productos de la base
	P=Producto.objects.all()
	# recorremos la lsita de productos para crear una lista alterna que luego vamos a utilizar
	for x in range(0,len(P)):
		ListForms.append(str(x))
	# For para recorrer nuevamente la lista de productos e inicializar los furmularios
	for x in range(0,len(P)):
		ListForms[x]=ProductoForm2(request.POST or None,request.FILES or None)
		ListForms[x].fields['nombre_producto'].initial=P[x].nombre_producto
		ListForms[x].fields['precio_venta'].initial=P[x].precio_venta
		ListForms[x].fields['utilidad_producto'].initial=P[x].utilidad_producto
		ListForms[x].fields['peso_producto'].initial=P[x].peso_producto
		ListForms[x].fields['precio_costo'].initial=P[x].precio_costo
	#p=Producto()
	if request.method == 'POST':
		for x in range(0,len(P)):
			if ListForms[x].is_valid():
				datosProd=ListForms[x].cleaned_data
				P[x].nombre_producto=datosProd.get("nombre_producto")
				P[x].precio_venta=datosProd.get("precio_venta")
				P[x].peso_producto=datosProd.get("peso_producto")
				P[x].precio_costo=datosProd.get("precio_costo")
				P[x].utilidad_producto=datosProd.get("utilidad_producto")
				if P[x].save() != True:
					ListForms[x].fields['peso_producto'].initial=P[x].peso_producto
					return redirect(IngresarRendimiento)

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
	'fr':fr,'lt':lt,'ct':CostoTotal,'ListForms':ListForms,
	'P':P,
	}
	return render(request,"IngresarRendimiento.html",context)

def ExportarRendimiento(request):

	return render(request,"ExportarRendimiento.html",context)

def RegistrarUsuario(request):
	fu= UsuarioForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if fu.is_valid():
			datosU= fu.cleaned_data
			User=Usuario()
			User.cedula=datosU.get("cedula")
			User.nombres=datosU.get("nombres")
			User.apellidos=datosU.get("apellidos")
			User.correo=datosU.get("correo")
			User.password=datosU.get("password")
			if User.save() != True:
				return redirect(Login)
	context={'fu':fu,}
	return render(request,"Registro.html",context)

def Login(request):
	userLogin=UsuarioLoginForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if userLogin.is_valid():
			datosLogin=userLogin.cleaned_data
			user=Usuario.objects.all()
			for x in range(0,len(user)):
				if user[x].correo==datosLogin.get("correo") and user[x].password==datosLogin.get("password"):
					return redirect(inicioAdmin)
				else:
					return redirect(Login)
	context={'userLogin':userLogin,}
	return render(request,"Login.html",context)
