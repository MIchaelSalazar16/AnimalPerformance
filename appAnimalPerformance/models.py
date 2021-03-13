from django.db import models
from django import forms
from django.utils import timezone

class LoteAnimal(models.Model):
    idLoteAnimal= models.AutoField(primary_key=True)
    peso_lote=  models.FloatField(default=0)
    precio_costo= models.FloatField(default=0)
    nombre_proveedor=models.CharField(max_length=50)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.idLoteAnimal

class Animal(models.Model):
    listaNombAnimal=(
    ('CERDO','CERDO'),
    )
    idAnimal= models.AutoField(primary_key=True)
    nombre_animal=  models.CharField(max_length=100,choices=listaNombAnimal, default="")
    peso_animal=  models.FloatField(null=False)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.idAnimal

class Producto(models.Model):
    listUnidades=(
    ('KG','KG'),
    ('UNIDAD','UNIDAD'),
    )
    idProducto= models.AutoField(primary_key=True)
    nombre_producto=  models.CharField(max_length=100)
    peso_producto=  models.FloatField(default=0,null=True)
    precio_costo=  models.FloatField(default=0,null=True)
    precio_venta=  models.FloatField(null=False)
    utilidad_producto=  models.FloatField(default=0)
    unidad= models.CharField(max_length=10,default='KG',choices=listUnidades,null=False)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.idProducto

class Rendimiento(models.Model):
    idRendimiento= models.AutoField(primary_key=True)
    total_costo=  models.FloatField(default=0,null=True)
    total_venta=  models.FloatField(default=0,null=True)
    margen_utilidad=  models.FloatField(default=0,null=True)
    rendimiento_neto=  models.FloatField(default=0,null=True)
    merma_deshidratacion=  models.FloatField(default=0,null=True)
    porcentaje_peso_neto=  models.FloatField(default=0,null=True)
    porcentaje_peso_producto=  models.FloatField(default=0,null=True)
    total_costo_producto=  models.FloatField(default=0,null=True)
    total_venta_producto=  models.FloatField(default=0,null=True)
    margen_utilidad_producto=  models.FloatField(default=0,null=True)
    fecha=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.idRendimiento

class Usuario(models.Model):
    idUsuario= models.AutoField(primary_key=True)
    cedula=  models.CharField(max_length=10)
    nombres=  models.CharField(max_length=30)
    apellidos=  models.CharField(max_length=30)
    correo=  models.EmailField(max_length=30)
    password=  models.CharField(max_length=30)
    def __str__(self):
        return self.idUsuario
