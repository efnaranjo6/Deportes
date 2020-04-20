from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Alineacion.models import Alineacion
from Alineacion.form import  Alineacionform

# vistas .

class Alineacionview(generic.ListView):
    model = Alineacion
    template_name = 'listar_Alineacion.html'
    context_object_name = 'Alineacion'
class Alineacioninsertar(generic.CreateView):
     model = Alineacion
     context_object_name = 'Alineacion'
     template_name = 'form_Alineacion.html'
     form_class = Alineacionform
     success_url=reverse_lazy("Alineacion:Alineacions")
class Alineacioneditar(generic.UpdateView):
     model = Alineacion
     context_object_name = 'Alineacion'
     template_name = 'form_Alineacion.html'
     form_class = Alineacionform
     success_url=reverse_lazy("Alineacion:Alineacions")
class Alineacioneliminar(generic.DeleteView):
     model = Alineacion
     context_object_name = 'Alineacion'
     template_name = 'delete_Alineacion.html'
     form_class = Alineacionform
     success_url=reverse_lazy("Alineacion:Alineacions")
# Create your views here.
