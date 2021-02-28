from django.forms import ModelForm
from .models import Rendimiento,LoteAnimal,Animal,Producto,Usuario

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['idAnimal','nombreAnimal','peso_animal',"precio_costo"]

class LoteAnimalForm(ModelForm):
    class Meta:
        model = LoteAnimal
        fields = ['idLoteAnimal','idAnimal','peso_lote']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','idAnimal','nombreProducto','peso_producto',
                    'utilidad_producto','precio_costo','precio_venta',
                    'porcentaje_peso','total_costo_producto','total_venta_producto','margen_utilidad_producto']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['idUsuario','cedula','nombres','apellidos','correo','password']

class RendimientoForm(ModelForm):
    class Meta:
        model = Rendimiento
        fields = ['idRendimiento','idLoteAnimal','idProducto','nombreProveedor','total_costo','total_venta','margen_utilidad',
                    'rendimiento_neto','merma_deshidratacion','porcentaje_peso_neto']
