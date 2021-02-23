from django.contrib import admin
from .models import Rendimiento
from .models import LoteAnimal
from .models import Animal
from .models import Producto
from .models import Usuario

class AdminRendimiento(admin.ModelAdmin):
	list_display=["idRendimiento","idLoteAnimal","idProducto","nombreProveedor","total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto","hora","fecha"]
	list_editable=["idLoteAnimal","idProducto","nombreProveedor","total_costo","total_venta","margen_utilidad",
                "rendimiento_neto","merma_deshidratacion","porcentaje_peso_neto","hora","fecha"]
	list_filter=["nombreProveedor"]
	search_fields=["nombreProveedor"]

	class Meta:
		model= Rendimiento

admin.site.register(Rendimiento,AdminRendimiento)
