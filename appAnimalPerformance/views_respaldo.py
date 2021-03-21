from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm ,ProductoForm2 ,ProductoForm3
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect, HttpRequest
from django.core import serializers
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from django.forms import modelformset_factory , formset_factory


def inicioAdmin(request):
	if request.user.is_authenticated:
		return render(request, "InicioAdmin.html",{})
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
				return redirect(inicioAdmin)
			else:
				return redirect(login)
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
				return redirect(inicioAdmin)
	return render(request, "login.html", {'form': form})

def logout(request):
	do_logout(request)
	return redirect('/AnimalPerformance/login')

def IngresarAnimal(request):
	if request.user.is_authenticated:
		fa=AnimalForm(request.POST or None, request.FILES or None)
		a=Animal()
		if request.method == 'POST':
			if fa.is_valid():
				#Limpieza de la lista que guarda el formulario
				datosA= fa.cleaned_data
				a.lote=datosA.get("lote")
				a.nombre_animal=datosA.get("nombre_animal")
				a.peso_animal=datosA.get("peso_animal")
				if a.save() != True:
					return redirect(IngresarAnimal)
		context={
		'fa':fa,
		}
		return render(request,"IngresarAnimal.html",context)
	else:
		return redirect(login)


def IngresarLote(request):
	if request.user.is_authenticated:
		a=Animal.objects.all().order_by('-fecha')[:2]
		flt=LoteAnimalForm(request.POST or None, request.FILES or None)
		lt=LoteAnimal()
		if request.method == 'POST':
			if flt.is_valid():
				datosLt= flt.cleaned_data
				lt.nombre_proveedor=datosLt.get("nombre_proveedor")
				lt.nombre_lote=datosLt.get("nombre_lote")
				lt.peso_lote=datosLt.get("peso_lote")
				lt.precio_costo=datosLt.get("precio_costo")
				if lt.save() != True:
					return redirect(ListarLotes)
		context={
		'flt':flt,
		'a':a,
		}
		return render(request,"IngresarLote.html",context)
	else:
		return redirect(login)

def IngresarProducto(request):
	if request.user.is_authenticated:
		#Variables de los formularios
		fp = ProductoForm(request.POST or None,request.FILES or None)
		p=Producto()
		if request.method == 'POST':
			if fp.is_valid() :
				datosP= fp.cleaned_data
				p.rendimiento=datosP.get("rendimiento")
				p.nombre_producto=datosP.get("nombre_producto")
				p.precio_venta=datosP.get("precio_venta")
				p.unidad=datosP.get("unidad")
				if p.save() != True:
					return redirect(IngresarProducto)
		context={
		'fp':fp,
		}
		return render(request,"IngresarProducto.html",context)
	else:
		return redirect(login)

def IngresarRendimiento(request):
	if request.user.is_authenticated:
		fr= RendimientoForm(request.POST or None)
		r=Rendimiento()
		if request.method == 'POST':
			if fr.is_valid():
				datosR= fr.cleaned_data
				r.lote=datosR.get("lote")
				r.nombre_rendimiento=datosR.get("nombre_rendimiento")
				if r.save() != True:
					return redirect(IngresarRendimiento)
				else:
					return redirect('AnimalPerformance/listarR')
		context={
		'fr':fr
		}
		return render(request,"IngresarRendimiento.html",context)
	else:
		return redirect(login)

def RegistrarPesos(request,idRendimiento):
	if request.user.is_authenticated:
		mensaje="NO EXISTEN PRODUCTOS PARA ESTE RENDIMIENTO"
		r=Rendimiento.objects.all()
		rend = Rendimiento.objects.get(idRendimiento=idRendimiento)
		if Producto.objects.filter(rendimiento_id=idRendimiento).exists()==True:
			lt= rend.lote
			Lt= LoteAnimal.objects.get(nombre_lote__exact=lt)
			PesoLote=Lt.peso_lote
			CostoTotal=round(Lt.precio_costo*PesoLote,2) #Total del costo del lote
			queryset=Producto.objects.all().filter(rendimiento_id=idRendimiento)
			print(queryset)
			# ProdFormset= modelformset_factory(Producto, form=ProductoForm2,exclude=(
			# 'porcentaje_peso_producto','total_costo_producto','total_venta_producto','utilidad_producto_xKG') ,extra=0)
			ProdFormset= modelformset_factory(Producto, form=ProductoForm3 ,extra=0)
			# ProdNew= formset_factory(form=ProductoForm3,extra=1)
			formset= ProdFormset(request.POST or None)
			#formsetNew= ProdNew(request.POST or None)
			if request.method== 'POST':
				print(formset.errors)
				if formset.is_valid():
					formset.save()
					return redirect('/AnimalPerformance/registrarPesos/'+str(idRendimiento))
				else:
					print("NO VALIDA")
		else:
			context={
			'M':mensaje, 'r':r
			}
			return render(request,"listarRendimientos.html",context)

		context={
		'formset':formset,'lt':Lt,'ct':CostoTotal,'rend':rend
		}
		return render(request,"RegistrarPesos.html",context)
	else:
		return redirect(login)

def CalculaRendimiento(request):
	if request.user.is_authenticated:
		# Creo la instancia de todos los productos de la base
		P=Producto.objects.all()
		lt=LoteAnimal.objects.latest('fecha') #trae el último lote ingresado
		PesoLote=lt.peso_lote
		CostoTotal=lt.precio_costo*PesoLote #Total del costo del lote
		#DECLARACION DE VARIABLES GLOBALES
		ListForms=[] #lista para guardar todos los formularios
		ListForms2=[]
		ListNombProd=[]
		ListPrecioVenta=[]
		ListPesoProd=[]
		ListIDprod=[]
		MargUtilGen=0 #Margen de utilidad en todo el rendimiento
		ListUtilXprodXkg=[] #Lista para guardar el margen $ de utilidad por KG en cada producto
		ListPrecioCostXprod=[] #Lista para guardar el precio de costo por producto
		ListTotalCostoXprod=[] #Lista que guarda el total de costo por producto segun el peso
		ListUtilXprod=[] #Lista para guaradar las utilidades $ por producto
		RendNeto=0 #Rendimiento neto
		VentaTotal=0 #Total de la venta segun el precio de venta al público producto
		MermaDES=0 #Merma por deshidratación
		TotalCos=0 #Suma TOTAL del total del costo por producto
		ListTotalVentaProd=[] #Lista que guarda total de la venta por producto
		ListPorcenPesoXProd=[] #Lista que alamacena porcentaje de peso por producto en referecia al peso del lote
	######################################################################################################################
		#TODOS LOS CALCULOS DE LA APP SE ENCUENTRAN EN ESTA SECCIÓN
		#Calula el total de venta por producto y el porcentaje que equivale el peso de cada producto en referecia al peso del lote
		for x in range(0,len(P)):
			ListTotalVentaProd.append(round((float(P[int(x)].peso_producto)*float(P[int(x)].precio_venta)),2))
			ListPorcenPesoXProd.append(round(float(P[int(x)].peso_producto)/CostoTotal,2))
			ListNombProd.append(P[x].nombre_producto)
			ListPrecioVenta.append(float(P[x].precio_venta))
			ListPesoProd.append(float(P[x].peso_producto))
			ListIDprod.append(int(P[x].idProducto))
		#Total de venta de todos los productos
		for x in range(0,len(ListTotalVentaProd)):
			VentaTotal+=round(ListTotalVentaProd[int(x)],2)
		#Calcula margen de utilidad del rendimiento
		if CostoTotal!=0 and VentaTotal!=0:
			MargUtilGen=round((((CostoTotal*100/VentaTotal)-100)*(-1)),2)
		#calcula margen de utilidad por KG en cada producto
		for x in range(0,len(P)):
			ListUtilXprodXkg.append(round(((float(P[int(x)].precio_venta)*MargUtilGen)/100),2))
		#Calcula el precio de costo por producto
		range(0,len(ListUtilXprodXkg))
		for x in range(0,len(P)):
			ListPrecioCostXprod.append(round(float(P[int(x)].precio_venta)-ListUtilXprodXkg[x],2))
		#Calcula el costo total por producto segun el peso.
		range(0,len(ListPrecioCostXprod))
		for x in range(0,len(P)):
			ListTotalCostoXprod.append(round((float(P[int(x)].peso_producto)*ListPrecioCostXprod[x]),2))
		#Calcula la utilidad neta $ por producto y la suma de los totales en costo total por producto
		#Preparamos las listas para poder iterar
		range(0,len(ListTotalVentaProd))
		range(0,len(ListTotalCostoXprod))
		for x in range(0,len(P)):
			ListUtilXprod.append(round(ListTotalVentaProd[x]-ListTotalCostoXprod[x],2))
			TotalCos+=round(ListTotalCostoXprod[x],2)
		#Merma por deshidratación
		MermaDES=round((PesoLote-RendNeto),2)
		#Rendimiento Neto
		for x in range(0,len(P)):
			RendNeto=round(RendNeto,2)+round(float(P[int(x)].peso_producto),2)
		#FIN DE LOS CALCULOS
	#############################################################################################################
		#Preparamos las listas para poder recorrerlas
		range(0,len(ListPrecioCostXprod))
		range(0,len(ListTotalCostoXprod))
		range(0,len(ListTotalVentaProd))
		range(0,len(ListPorcenPesoXProd))
		range(0,len(ListUtilXprodXkg))
		range(0,len(ListUtilXprod))
		# for x in range(0,len(P)):
		# 	ListForms.append(ProductoForm2(request.POST or None))
		#ListForms.clear()
		for x in range(0,len(P)):
			ListForms.append(ProductoForm2(request.POST or None))
			range(0,len(ListForms))
			ListForms[x].fields['nombre_producto'].initial=ListNombProd[x]
			ListForms[x].fields['peso_producto'].initial=ListPesoProd[x]
			ListForms[x].fields['utilidad_producto_xKG'].initial=round(ListUtilXprodXkg[x],2)
			ListForms[x].fields['precio_costo'].initial=round(ListPrecioCostXprod[x],2)
			ListForms[x].fields['total_costo_producto'].initial=round(ListTotalCostoXprod[x],2)
			ListForms[x].fields['porcentaje_peso_producto'].initial=round((ListPorcenPesoXProd[x]*100),2)
			ListForms[x].fields['precio_venta'].initial=ListPrecioVenta[x]
			ListForms[x].fields['utilidad_producto'].initial=round(ListUtilXprod[x],2)
			ListForms[x].fields['total_venta_producto'].initial=round(ListTotalVentaProd[x],2)
			print(ListNombProd[x])
			print(ListPesoProd[x])
			print(ListUtilXprodXkg[x])
			print(ListPrecioVenta[x])
			print(ListPrecioCostXprod[x])
			print(ListTotalCostoXprod[x])
			print(ListPorcenPesoXProd[x])
			print(ListUtilXprod[x])
			print(ListTotalVentaProd[x])
			print("#################################")
			if ListForms[x].is_valid():
				ListForms[x].save()
				print("ES VALIDO")
			else:
				print("No es valido")

		if request.method== 'POST':
			for x in range(0,len(ListForms2)):
				print(x)
				#print(ListForms2[x])
				# if ProdAux.save() !=True:
				# 	return redirect(CalculaRendimiento)

		fr= RendimientoForm(request.POST or None)
		r=Rendimiento()
		fr.fields["total_costo"].initial=round(TotalCos,2)
		fr.fields["total_venta"].initial=round(VentaTotal,2)
		fr.fields["margen_utilidad"].initial=MargUtilGen
		fr.fields["rendimiento_neto"].initial=round(RendNeto)
		fr.fields["merma_deshidratacion"].initial=round(PesoLote-RendNeto,2)
		fr.fields["porcentaje_peso_neto"].initial=round((RendNeto*100)/PesoLote,2)
		if request.method == 'POST':
			#ListForms.clear()
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
		'P':P,'RendNeto':RendNeto,'ct2':TotalCos,'MD':MermaDES,
		# 'formset':formset,
		}
		return render(request,"CalculaRendimiento_2.html",context)
	else:
		return redirect(login)


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
	if request.user.is_authenticated:
		fr = RendimientoForm(request.POST or None,request.FILES or None)
		r = Rendimiento.objects.get(idRendimiento=request.GET['idRendimiento'])
		fr.fields["lote"].initial=r.lote
		fr.fields["nombre_rendimiento"].initial=r.nombre_rendimiento
		if request.method == 'POST':
			if fr.is_valid():
				datos= fr.cleaned_data
				r.lote=datos.get("lote")
				r.nombre_rendimiento=datos.get("nombre_rendimiento")
				if r.save() != True:
					return redirect(ListarRendimiento)
		context={
		'fr':fr,
	    }
		return render(request,"modificarRendimiento.html",context)
	else:
		return redirect(login)
def modificarAnimal(request):
	if request.user.is_authenticated:
		fa= AnimalForm(request.POST or None,request.FILES or None)
		a = Animal.objects.get(idAnimal=request.GET['idAnimal'])
		fa.fields["lote"].initial=a.lote
		fa.fields["nombre_animal"].initial=a.nombre_animal
		fa.fields["peso_animal"].initial=a.peso_animal
		if request.method == 'POST':
			if fa.is_valid():
				datos= fa.cleaned_data
				a.lote=datos.get("lote")
				a.nombre_animal=datos.get("nombre_animal")
				a.peso_animal=datos.get("peso_animal")
				if a.save() != True:
					return redirect(ListarAnimales)
		context={
		'fa':fa,
	    'a':a,
	    }
		return render(request,"modificarAnimal.html",context)
	else:
		return redirect(login)

def modificarProducto(request):
	if request.user.is_authenticated:
		fp= ProductoForm(request.POST or None,request.FILES or None)
		p = Producto.objects.get(idProducto=request.GET['idProducto'])
		fp.fields["nombre_producto"].initial=p.nombre_producto
		fp.fields["rendimiento"].initial=p.rendimiento
		fp.fields["precio_venta"].initial=p.precio_venta
		fp.fields["unidad"].initial=p.unidad
		if request.method == 'POST':
			if fp.is_valid():
				datos= fp.cleaned_data
				p.nombre_producto=datos.get("nombre_producto")
				p.rendimiento=datos.get("rendimiento")
				p.precio_venta=datos.get("precio_venta")
				p.unidad=datos.get("unidad")
				if p.save() != True:
					return redirect(ListarProductos)
		context={
		'fp':fp,
	    'p':p,
	    }
		return render(request,"modificarProducto.html",context)
	else:
		return redirect(login)
def modificarLote(request):
	if request.user.is_authenticated:
		flt= LoteAnimalForm(request.POST or None,request.FILES or None)
		lt = LoteAnimal.objects.get(idLoteAnimal=request.GET['idLoteAnimal'])
		flt.fields["peso_lote"].initial=lt.peso_lote
		flt.fields["precio_costo"].initial=lt.precio_costo
		flt.fields["nombre_proveedor"].initial=lt.nombre_proveedor
		flt.fields["nombre_lote"].initial=lt.nombre_lote
		if request.method == 'POST':
			if flt.is_valid():
				datos= flt.cleaned_data
				lt.peso_lote=datos.get("peso_lote")
				lt.precio_costo=datos.get("precio_costo")
				lt.nombre_proveedor=datos.get("nombre_proveedor")
				lt.nombre_lote=datos.get("nombre_lote")
				if lt.save() != True:
					return redirect(ListarLotes)
		context={
		'flt':flt,
	    'lt':lt,
	    }
		return render(request,"modificarLote.html",context)
	else:
		return redirect(login)
############_____ELIMINAR ENTIDADES______###############################################
def eliminarAnimal(request):
	if request.user.is_authenticated:
		animal = Animal.objects.get(idAnimal=request.GET['idAnimal'])
		animal.delete()
		return redirect(ListarAnimales)
	else:
		return redirect(login)

def eliminarLote(request):
	if request.user.is_authenticated:
		lote = LoteAnimal.objects.get(idLoteAnimal=request.GET['idLoteAnimal'])
		lote.delete()
		return redirect(ListarLotes)
	else:
		return redirect(login)

def eliminarProducto(request):
	if request.user.is_authenticated:
		producto = Producto.objects.get(idProducto=request.GET['idProducto'])
		producto.delete()
		return redirect(ListarProductos)
	else:
		return redirect(login)

def eliminarRendimiento(request):
	if request.user.is_authenticated:
		rendimiento = Rendimiento.objects.get(idRendimiento=request.GET['idRendimiento'])
		rendimiento.delete()
		return redirect(ListarRendimiento)
	else:
		return redirect(login)
