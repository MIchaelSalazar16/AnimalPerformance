from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from appAnimalPerformance.views import inicioAdmin,IngresarRendimiento,IngresarAnimal,IngresarLote,IngresarProducto
from appAnimalPerformance.views import NumAnimales, welcome,login,logout,register, ListarLotes,ListarProductos
from appAnimalPerformance.views import ListarAnimales, ListarRendimiento

urlpatterns=[
	path('', inicioAdmin),
	path('ingresarR/',IngresarRendimiento),
	path('ingresarA/',IngresarAnimal),
	#path('ingresarA/<int:na>',IngresarAnimal),
	path('ingresarLt/',IngresarLote),
	path('ingresarP/',IngresarProducto),
	#path('na/',NumAnimales),
	path('registro/',register),
	path('login/',login),
	path('welcome/',welcome),
	path('login/',logout),
	path('listarAnimales/',ListarAnimales),
	path('listarLotes/',ListarLotes),
	path('listarProductos/',ListarProductos),
	path('listarRendimientos/',ListarRendimiento),
]
