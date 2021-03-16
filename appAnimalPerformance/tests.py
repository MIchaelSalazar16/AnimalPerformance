from django.test import TestCase
from django.http import HttpResponse,HttpResponseRedirect, HttpRequest
from .models import Animal,Producto,Rendimiento,LoteAnimal
from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,ProductoForm2
from django.forms import modelformset_factory

class ViewsTestCase(TestCase):
    # def test_index_loads_properly(self):
    #     response = self.client.get('127.0.0.1:8000/AnimalPerformance/')
    #     self.assertEqual(response.status_code, 200)

    def test_guarda_formularios_formsets(self):
        ProdFormset= modelformset_factory(Producto, form=ProductoForm2, extra=0)
        formProd= ProdFormset(request.POST or None)
        if request.method == 'POST':
            formProd.save()

    def traer_ultimo_lote(self):
        lt=LoteAnimal.objects.latest('fecha')
