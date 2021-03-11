from django.contrib import admin
from .models import Rendimiento
from .models import LoteAnimal
from .models import Animal
from .models import Producto
from .models import Usuario


class AdminAnimal(admin.ModelAdmin):
	list_display=["idAnimal","nombre_animal","peso_animal"]
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

class AdminUsuario(admin.ModelAdmin):
	list_display=["idUsuario", "cedula", "nombres", "apellidos", "correo", "password"]
	list_editable=["cedula", "nombres", "apellidos", "correo", "password"]
	list_filter=["nombres","apellidos"]
	search_fields=["nombres","apellidos"]

	class Meta:
		model= Usuario

admin.site.register(Usuario,AdminUsuario)

class AdminProducto(admin.ModelAdmin):
	list_display=["idProducto","nombre_producto","peso_producto","utilidad_producto","precio_costo","precio_venta"]
	list_editable=["nombre_producto","peso_producto","utilidad_producto","precio_costo","precio_venta"]
	list_filter=["nombre_producto"]
	search_fields=["nombre_producto"]

	class Meta:
		model= Producto

admin.site.register(Producto,AdminProducto)

class AdminRendimiento(admin.ModelAdmin):
	list_display=["idRendimiento","total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto",
                "porcentaje_peso_producto","total_costo_producto","total_venta_producto","margen_utilidad_producto"]
	list_editable=["total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto"]
	list_filter=["total_costo"]
	search_fields=["total_costo"]

	class Meta:
		model= Rendimiento

admin.site.register(Rendimiento,AdminRendimiento)
