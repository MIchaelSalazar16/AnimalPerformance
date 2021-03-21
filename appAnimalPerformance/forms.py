from django.forms import ModelForm
from .models import Rendimiento,LoteAnimal,Animal,Producto
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['idAnimal','lote','nombre_animal','peso_animal']

class LoteAnimalForm(ModelForm):
    class Meta:
        model = LoteAnimal
        fields = ['idLoteAnimal','nombre_lote','peso_lote','precio_costo','nombre_proveedor']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','rendimiento','nombre_producto','precio_venta','unidad']

class ProductoForm2(ModelForm):
    nombre_producto=forms.CharField(widget=forms.TextInput(attrs={ 'readonly':'readonly','class':'border-0','size':'25'}))
    peso_producto=forms.FloatField(widget=forms.NumberInput(attrs={'style':'width: 5em', 'min':'0', 'max':'9999.9999'}))
    precio_venta=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0 text-danger','style':'width: 5em'}))
    precio_costo=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    utilidad_producto=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    porcentaje_peso_producto=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    total_costo_producto=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    total_venta_producto=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    utilidad_producto_xKG=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    class Meta:
        model = Producto
        fields = ['peso_producto','precio_costo','nombre_producto','precio_venta','utilidad_producto',
                  'porcentaje_peso_producto','total_costo_producto','total_venta_producto','utilidad_producto_xKG']

class ProductoForm3(ModelForm):
    nombre_producto=forms.CharField(widget=forms.TextInput(attrs={ 'readonly':'readonly','class':'border-0','size':'20'}))
    peso_producto=forms.FloatField(widget=forms.NumberInput(attrs={'style':'width: 5em', 'min':'0', 'max':'9999.9999'}))
    precio_venta=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0 text-danger','style':'width: 5em'}))
    precio_costo=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    utilidad_producto=forms.FloatField(widget=forms.NumberInput(attrs={ 'readonly':'readonly','class':'border-0','style':'width: 5em'}))
    class Meta:
        model = Producto
        fields = ['peso_producto','precio_costo','nombre_producto','precio_venta','utilidad_producto']

class RendimientoForm(ModelForm):
    class Meta:
        model = Rendimiento
        fields = ['idRendimiento','lote','nombre_rendimiento']

class RendimientoForm2(ModelForm):
    class Meta:
        model = Rendimiento
        fields = ['idRendimiento','total_costo','total_venta','margen_utilidad',
                    'rendimiento_neto','merma_deshidratacion','porcentaje_peso_neto','porcent_merma_deshidratacion']
