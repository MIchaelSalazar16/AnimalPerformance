from django.db import models
from django import forms
from django.utils import timezone


class LoteAnimal(models.Model):
    lista_nombre_animal=(
    ('CERDO','CERDO'),
    )
    idLoteAnimal= models.AutoField(primary_key=True)
    nombre_animal=  models.CharField(max_length=100,choices=lista_nombre_animal, default="")
    peso_lote=  models.FloatField()
    precio_costo= models.FloatField()
    fecha=models.DateField(auto_now_add=True,null=True)

class Animal(models.Model):
    idAnimal= models.AutoField(primary_key=True)
    idLoteAnimal=models.ForeignKey(LoteAnimal,on_delete=models.CASCADE,default="")
    peso_animal=  models.FloatField()
    #fecha=models.DateTimeField(auto_now_add=True,null=True)

class Producto(models.Model):
    idProducto= models.AutoField(primary_key=True)
    nombre_producto=  models.CharField(max_length=100)
    peso_producto=  models.FloatField()
    utilidad_producto=  models.FloatField()
    precio_costo=  models.FloatField()
    precio_venta=  models.FloatField()
    porcentaje_peso=  models.FloatField()
    total_costo_producto=  models.FloatField()
    total_venta_producto=  models.FloatField()
    margen_utilidad_producto=  models.FloatField()
    #fecha=models.DateTimeField(auto_now_add=True,null=True)

class Usuario(models.Model):
    idUsuario= models.AutoField(primary_key=True)
    cedula=  models.CharField(max_length=10)
    nombres=  models.CharField(max_length=30)
    apellidos=  models.CharField(max_length=30)
    correo=  models.CharField(max_length=30)
    password=  models.CharField(max_length=30)
    #fecha=models.DateTimeField(auto_now_add=True,null=True)

class Rendimiento(models.Model):
    idRendimiento= models.AutoField(primary_key=True)
    idLoteAnimal= models.ForeignKey(LoteAnimal,on_delete=models.CASCADE,default="")
    nombre_proveedor=  models.CharField(max_length=100)
    total_costo=  models.FloatField()
    total_venta=  models.FloatField()
    margen_utilidad=  models.FloatField()
    rendimiento_neto=  models.FloatField()
    merma_deshidratacion=  models.FloatField()
    porcentaje_peso_neto=  models.FloatField()
    #fecha=models.DateTimeField(auto_now_add=True,null=True)
