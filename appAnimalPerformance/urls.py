from django.conf.urls import url
from django.contrib import admin
from appAnimalPerformance.views import inicioAdmin


urlpatterns=[
	url(r'^$',inicioAdmin,name="inicioAdmin"),

]