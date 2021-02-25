from django.shortcuts import render

from django.shortcuts import redirect,render
from .models import Animal,Producto,Rendimiento,LoteAnimal,Usuario
#from .forms import AnimalForm,LoteAnimalForm,ProductoForm,RendimientoForm,UsuarioForm
from django.core.files.uploadedfile import SimpleUploadedFile
import json as simplejson
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers

# Create your views here.
def inicioAdmin(request):
    p=Rendimiento.objects.all()
    context={
    'p':p,
    }
    return render(request,"InicioAdmin.html",context)



