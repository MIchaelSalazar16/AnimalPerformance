from django.forms import ModelForm
from .models import Rendimiento,LoteAnimal,Animal,Producto,Usuario
from django import forms

class AnimalForm(ModelForm):
    #nombre_animal=forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Animal
        fields = ['idAnimal','idLoteAnimal','peso_animal']

class LoteAnimalForm(ModelForm):
    class Meta:
        model = LoteAnimal
        fields = ['idLoteAnimal','peso_lote','nombre_animal','precio_costo']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombre_producto','peso_producto',
                    'utilidad_producto','precio_costo','precio_venta',
                    'porcentaje_peso','total_costo_producto','total_venta_producto','margen_utilidad_producto']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['idUsuario','cedula','nombres','apellidos','correo','password']

class RendimientoForm(ModelForm):
    class Meta:
        model = Rendimiento
        fields = ['idRendimiento','idLoteAnimal','nombre_proveedor','total_costo','total_venta','margen_utilidad',
                    'rendimiento_neto','merma_deshidratacion','porcentaje_peso_neto']
