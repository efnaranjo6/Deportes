from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Estadio.models import Estadio
from Estadio.form import  Estadioform

# vistas .

class Estadioview(generic.ListView):
    model = Estadio
    template_name = 'listar_Estadio.html'
    context_object_name = 'estadio'
class Estadioinsertar(generic.CreateView):
     model = Estadio
     context_object_name = 'estadio'
     template_name = 'form_Estadio.html'
     form_class = Estadioform
     success_url=reverse_lazy("Estadio:Estadios")
class Estadioeditar(generic.UpdateView):
     model = Estadio
     context_object_name = 'estadio'
     template_name = 'form_Estadio.html'
     form_class = Estadioform
     success_url=reverse_lazy("Estadio:Estadios")
class Estadioeliminar(generic.DeleteView):
     model = Estadio
     context_object_name = 'estadio'
     template_name = 'delete_Estadio.html'
     form_class = Estadioform
     success_url=reverse_lazy("Estadio:Estadios")
# Create your views here.
