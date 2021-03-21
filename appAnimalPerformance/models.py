from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class LoteAnimal(models.Model):
    idLoteAnimal= models.AutoField(primary_key=True)
    nombre_lote=models.CharField(max_length=50,default='')
    peso_lote=  models.FloatField(blank=False,default=0)
    precio_costo= models.FloatField(blank=False,default=0)
    nombre_proveedor=models.CharField(max_length=50)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_lote

class Animal(models.Model):
    listaNombAnimal=(
    ('CERDO','CERDO'),
    )
    idAnimal= models.AutoField(primary_key=True)
    lote=models.ForeignKey(LoteAnimal,on_delete=models.CASCADE,default='')
    nombre_animal=  models.CharField(max_length=100,choices=listaNombAnimal, default="")
    peso_animal=  models.FloatField(blank=False,default=0)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_animal

class Rendimiento(models.Model):
    idRendimiento= models.AutoField(primary_key=True)
    lote=models.ForeignKey(LoteAnimal,on_delete=models.CASCADE,default='')
    nombre_rendimiento=models.CharField(max_length=50,default='')
    total_costo=  models.FloatField(blank=False,default=0)
    total_venta=  models.FloatField(blank=False,default=0)
    margen_utilidad=  models.FloatField(blank=False,default=0)
    rendimiento_neto=  models.FloatField(blank=False,default=0)
    merma_deshidratacion=  models.FloatField(blank=False,default=0)
    porcentaje_peso_neto=  models.FloatField(blank=False,default=0)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_rendimiento

class Producto(models.Model):
    listUnidades=(
    ('KG','KG'),
    ('UNIDAD','UNIDAD'),
    )
    idProducto= models.AutoField(primary_key=True)
    nombre_producto=  models.CharField(max_length=100,blank=False)
    rendimiento=models.ForeignKey(Rendimiento,on_delete=models.CASCADE,default='')
    peso_producto=  models.FloatField(blank=False,default=0)
    precio_costo=  models.FloatField(blank=False,default=0)
    precio_venta=  models.FloatField(blank=False,default=0)
    utilidad_producto=  models.FloatField(blank=True,default=0)
    porcentaje_peso_producto=  models.FloatField(blank=True,default=0)
    total_costo_producto=  models.FloatField(blank=True,default=0)
    total_venta_producto=  models.FloatField(blank=True,default=0)
    utilidad_producto_xKG=  models.FloatField(blank=True,default=0)
    unidad= models.CharField(max_length=10,default='KG',choices=listUnidades,null=False)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_producto
