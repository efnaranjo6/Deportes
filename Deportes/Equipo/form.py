from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Equipo.models import Equipo
from Equipo.form import  Equipoform

# vistas .

class Equipoview(generic.ListView):
    model = Equipo
    template_name = 'listar_Equipo.html'
    context_object_name = 'Equipo'
class Equipoinsertar(generic.CreateView):
     model = Equipo
     context_object_name = 'Equipo'
     template_name = 'form_Equipo.html'
     form_class = Equipoform
     success_url=reverse_lazy("Equipo:Equipos")
class Equipoeditar(generic.UpdateView):
     model = Equipo
     context_object_name = 'Equipo'
     template_name = 'form_Equipo.html'
     form_class = Equipoform
     success_url=reverse_lazy("Equipo:Equipos")
class Equipoeliminar(generic.DeleteView):
     model = Equipo
     context_object_name = 'Equipo'
     template_name = 'delete_Equipo.html'
     form_class = Equipoform
     success_url=reverse_lazy("Equipo:Equipos")
# Create your views here.
