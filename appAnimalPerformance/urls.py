from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from appAnimalPerformance.views import inicioAdmin
from appAnimalPerformance.views import IngresarRendimiento
from appAnimalPerformance.views import IngresarAnimal
from appAnimalPerformance.views import IngresarLote
from appAnimalPerformance.views import IngresarProducto
from appAnimalPerformance.views import NumAnimales

urlpatterns=[
	path('', inicioAdmin),
	path('ingresarR/',IngresarRendimiento),
	path('ingresarA/',IngresarAnimal),
	path('ingresarLt/<int:aux>',IngresarLote),
	path('ingresarP/',IngresarProducto),
	path('num/',NumAnimales),	
]