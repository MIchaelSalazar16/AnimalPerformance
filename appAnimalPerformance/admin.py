from django.contrib import admin
from .models import Rendimiento
from .models import LoteAnimal
from .models import Animal
from .models import Producto
from django.contrib.auth.models import User


class AdminAnimal(admin.ModelAdmin):
	list_display=["idAnimal","lote","nombre_animal","peso_animal"]
	list_editable=[ "nombre_animal","peso_animal"]
	list_filter=[ "nombre_animal","peso_animal"]
	search_fields=[ "nombre_animal","peso_animal"]

	class Meta:
		model= Animal
admin.site.register(Animal,AdminAnimal)

class AdminLoteAnimal(admin.ModelAdmin):
	list_display=["idLoteAnimal","peso_lote","precio_costo","nombre_proveedor"]
	list_editable=["peso_lote","precio_costo","nombre_proveedor"]
	list_filter=["nombre_proveedor"]
	search_fields=["nombre_proveedor"]
	class Meta:
		model= LoteAnimal
admin.site.register(LoteAnimal,AdminLoteAnimal)

class AdminProducto(admin.ModelAdmin):
	list_display=["idProducto","rendimiento","nombre_producto","peso_producto","utilidad_producto","precio_costo","precio_venta"]
	list_editable=["nombre_producto","peso_producto","utilidad_producto","precio_costo","precio_venta"]
	list_filter=["nombre_producto"]
	search_fields=["nombre_producto"]
	raw_id_fields=["rendimiento"]
	class Meta:
		model= Producto
admin.site.register(Producto,AdminProducto)

class AdminRendimiento(admin.ModelAdmin):
	list_display=["idRendimiento","lote","total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto"]
	list_editable=["total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto"]
	list_filter=["total_costo"]
	search_fields=["lote","total_costo"]
	raw_id_fields=["lote"]
	class Meta:
		model= Rendimiento
admin.site.register(Rendimiento,AdminRendimiento)
