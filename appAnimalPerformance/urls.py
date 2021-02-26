from django.conf.urls import url
from django.contrib import admin
from appAnimalPerformance.views import inicioAdmin
from appAnimalPerformance.views import IngresarRendimiento


urlpatterns=[
	url(r'^$',inicioAdmin,name="inicioAdmin"),
	url(r'^ingresarRend/',IngresarRendimiento,name="IngresarRendimiento"),
]