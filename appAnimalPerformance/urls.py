from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from appAnimalPerformance.views import inicioAdmin,IngresarRendimiento,IngresarAnimal,IngresarLote,IngresarProducto
from appAnimalPerformance.views import NumAnimales, login,logout,register, ListarLotes,ListarProductos
from appAnimalPerformance.views import ListarAnimales, ListarRendimiento, modificarLote, modificarAnimal
from appAnimalPerformance.views import modificarProducto, modificarRendimiento

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
	path('login/',logout),
	path('listarA/',ListarAnimales),
	path('listarLt/',ListarLotes),
	path('listarP/',ListarProductos),
	path('listarR/',ListarRendimiento),
	path('modificarA/',modificarAnimal),
	path('modificarLt/',modificarLote),
	path('modificarP/',modificarProducto),
	path('modificarR/',modificarRendimiento),
]
