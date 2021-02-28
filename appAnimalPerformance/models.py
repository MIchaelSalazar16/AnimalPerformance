from django.db import models
from django import forms

class Animal(models.Model):
    idAnimal= models.AutoField(primary_key=True)
    nombreAnimal=  models.CharField(max_length=100)
    peso_animal=  models.FloatField()
    precio_costo= models.FloatField()

class LoteAnimal(models.Model):
    idLoteAnimal= models.AutoField(primary_key=True)
    idAnimal= models.ForeignKey(Animal,on_delete=models.CASCADE,default="")
    peso_lote=  models.FloatField()

class Producto(models.Model):
    idProducto= models.AutoField(primary_key=True)
    idAnimal= models.ForeignKey(Animal,on_delete=models.CASCADE,default="")
    nombreProducto=  models.CharField(max_length=100)
    peso_producto=  models.FloatField()
    utilidad_producto=  models.FloatField()
    precio_costo=  models.FloatField()
    precio_venta=  models.FloatField()
    porcentaje_peso=  models.FloatField()
    total_costo_producto=  models.FloatField()
    total_venta_producto=  models.FloatField()
    margen_utilidad_producto=  models.FloatField()

class Usuario(models.Model):
    idUsuario= models.AutoField(primary_key=True)
    cedula=  models.CharField(max_length=10)
    nombres=  models.CharField(max_length=30)
    apellidos=  models.CharField(max_length=30)
    correo=  models.CharField(max_length=30)
    password=  models.CharField(max_length=30)

class Rendimiento(models.Model):
    idRendimiento= models.AutoField(primary_key=True)
    idLoteAnimal= models.ForeignKey(LoteAnimal,on_delete=models.CASCADE,default="")
    idProducto= models.ForeignKey(Producto,on_delete=models.CASCADE,default="")
    nombreProveedor=  models.CharField(max_length=100)
    total_costo=  models.FloatField()
    total_venta=  models.FloatField()
    margen_utilidad=  models.FloatField()
    rendimiento_neto=  models.FloatField()
    merma_deshidratacion=  models.FloatField()
    porcentaje_peso_neto=  models.FloatField()
    #hora=  models.DateField()
    #fecha=  models.DateField()
