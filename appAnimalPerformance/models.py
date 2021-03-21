from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class LoteAnimal(models.Model):
    idLoteAnimal= models.AutoField(primary_key=True)
    nombre_lote=models.CharField(max_length=50,default='')
    peso_lote=  models.DecimalField(max_digits=5,decimal_places=2,blank=False,default=0)
    precio_costo= models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0)
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
    peso_animal=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_animal

class Rendimiento(models.Model):
    idRendimiento= models.AutoField(primary_key=True)
    lote=models.ForeignKey(LoteAnimal,on_delete=models.CASCADE,default='')
    nombre_rendimiento=models.CharField(max_length=50,default='')
    total_costo=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    total_venta=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    margen_utilidad=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    rendimiento_neto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    merma_deshidratacion=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    porcentaje_peso_neto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_rendimiento

class Producto(models.Model):
    listUnidades=(
    ('KG','KG'),
    ('UNIDAD','UNIDAD'),
    )
    idProducto= models.AutoField(primary_key=True)
    nombre_producto=  models.CharField(max_length=100)
    rendimiento=models.ForeignKey(Rendimiento,on_delete=models.CASCADE,default='')
    peso_producto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    precio_costo=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    precio_venta=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    utilidad_producto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0)
    porcentaje_peso_producto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    total_costo_producto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    total_venta_producto=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    utilidad_producto_xKG=  models.DecimalField(max_digits=5,decimal_places=3,blank=False,default=0,null=True)
    unidad= models.CharField(max_length=10,default='KG',choices=listUnidades,null=False)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nombre_producto
