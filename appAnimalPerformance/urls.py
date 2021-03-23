from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from appAnimalPerformance.views import inicioAdmin,IngresarRendimiento,IngresarAnimal,IngresarLote,IngresarProducto
from appAnimalPerformance.views import  login,logout,register, ListarLotes,ListarProductos
from appAnimalPerformance.views import ListarAnimales, ListarRendimiento, modificarLote, modificarAnimal
from appAnimalPerformance.views import modificarProducto, modificarRendimiento , eliminarLote, eliminarRendimiento
from appAnimalPerformance.views import eliminarAnimal, eliminarProducto ,RegistrarPesos,CalculaRendimiento, ExportarRendimientoPdf


urlpatterns=[
	path('', inicioAdmin),
	path('ingresarR/',IngresarRendimiento),
	path('ingresarA/',IngresarAnimal),
	path('ingresarLt/',IngresarLote),
	path('ingresarP/',IngresarProducto),
	path('registro/',register),
	path('login/',login),
	path('logout/',logout),
	path('listarA/',ListarAnimales),
	path('listarLt/',ListarLotes),
	path('listarP/',ListarProductos),
	path('listarR/',ListarRendimiento),
	path('modificarA/',modificarAnimal),
	path('modificarLt/',modificarLote),
	path('modificarP/',modificarProducto),
	path('modificarR/',modificarRendimiento),
	path('eliminarA/',eliminarAnimal),
	path('eliminarLt/',eliminarLote),
	path('eliminarP/',eliminarProducto),
	path('eliminarR/',eliminarRendimiento),
	path('registrarPesos/',ListarRendimiento),
	path('registrarPesos/<int:idRendimiento>',RegistrarPesos),
	path('calculaR/<int:idRendimiento>',CalculaRendimiento),
	path('calculaR/',ListarRendimiento),
	path('exportarPdf/<int:idRendimiento>',ExportarRendimientoPdf),
]
