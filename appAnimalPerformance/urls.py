from django.conf.urls import url
from django.contrib import admin
from appAnimalPerformance.views import inicioAdmin
from appAnimalPerformance.views import IngresarRendimiento
from appAnimalPerformance.views import IngresarAnimal
from appAnimalPerformance.views import IngresarLote
from appAnimalPerformance.views import IngresarProducto

urlpatterns=[
	url(r'^$',inicioAdmin,name="inicioAdmin"),
	url(r'^ingresarR/',IngresarRendimiento,name="IngresarRendimiento"),
	url(r'^ingresarA/',IngresarAnimal,name="IngresarAnimal"),
	url(r'^ingresarLt/',IngresarLote,name="IngresarLote"),
	url(r'^ingresarP/',IngresarProducto,name="IngresarProducto"),
	
]