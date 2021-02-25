from django.contrib import admin
from .models import Rendimiento
from .models import LoteAnimal
from .models import Animal
from .models import Producto
from .models import Usuario


class AdminAnimal(admin.ModelAdmin):
	list_display=["idAnimal", "nombreAnimal", "peso_animal", "precio_costo"]
	list_editable=["nombreAnimal", "peso_animal", "precio_costo"]
	list_filter=["nombreAnimal"]
	search_fields=["nombreAnimal"]

	class Meta:
		model= Animal

admin.site.register(Animal,AdminAnimal)

class AdminLoteAnimal(admin.ModelAdmin):
	list_display=["idLoteAnimal", "idAnimal", "peso_lote"]
	list_editable=["peso_lote"]
	list_filter=["idLoteAnimal"]
	search_fields=["idLoteAnimal"]

	class Meta:
		model= LoteAnimal

admin.site.register(LoteAnimal,AdminLoteAnimal)

class AdminUsuario(admin.ModelAdmin):
	list_display=["idUsuario", "cedula", "nombres", "apellidos", "correo", "password"]
	list_editable=["cedula", "nombres", "apellidos", "correo", "password"]
	list_filter=["nombres","apellidos"]
	search_fields=["nombres","apellidos"]

	class Meta:
		model= Usuario

admin.site.register(Usuario,AdminUsuario)

class AdminProducto(admin.ModelAdmin):
	list_display=["idProducto","idAnimal","nombreProducto","peso_producto",
                    "utilidad_producto","precio_costo","precio_venta",
                    "porcentaje_peso","total_costo_producto","total_venta_producto","margen_utilidad_producto"]
	list_editable=["nombreProducto","peso_producto",
                    "utilidad_producto","precio_costo","precio_venta",
                    "porcentaje_peso","total_costo_producto","total_venta_producto","margen_utilidad_producto"]
	list_filter=["nombreProducto"]
	search_fields=["nombreProducto"]

	class Meta:
		model= Producto

admin.site.register(Producto,AdminProducto)

class AdminRendimiento(admin.ModelAdmin):
	list_display=["idRendimiento","idLoteAnimal","idProducto","nombreProveedor","total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto","hora","fecha"]
	list_editable=["nombreProveedor","total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto","hora","fecha"]
	list_filter=["nombreProveedor"]
	search_fields=["nombreProveedor"]

	class Meta:
		model= Rendimiento

admin.site.register(Rendimiento,AdminRendimiento)
