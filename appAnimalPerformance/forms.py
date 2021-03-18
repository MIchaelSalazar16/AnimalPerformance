from django.forms import ModelForm
from .models import Rendimiento,LoteAnimal,Animal,Producto
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['idAnimal','nombre_animal','peso_animal']

class LoteAnimalForm(ModelForm):
    class Meta:
        model = LoteAnimal
        fields = ['idLoteAnimal','peso_lote','precio_costo','nombre_proveedor']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombre_producto','precio_venta','unidad']

class ProductoForm2(ModelForm):
    class Meta:
        model = Producto
        fields = ['peso_producto','precio_costo','nombre_producto','precio_venta','utilidad_producto',
                  'porcentaje_peso_producto','total_costo_producto','total_venta_producto','utilidad_producto_xKG']
        # nombre_producto= forms.CharField(widget=forms.TextInput(attrs={ 'readonly':'readonly'}))
        # precio_venta= forms.CharField(widget=forms.TextInput(attrs={ 'readonly':'readonly'}))

class RendimientoForm(ModelForm):
    class Meta:
        model = Rendimiento
        fields = ['idRendimiento','total_costo','total_venta','margen_utilidad',
                    'rendimiento_neto','merma_deshidratacion','porcentaje_peso_neto']
