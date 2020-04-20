from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Partido.models import Partido
from Partido.form import  Partidoform

# vistas .

class Partidoview(generic.ListView):
    model = Partido
    template_name = 'listar_Partido.html'
    context_object_name = 'Partido'
class Partidoinsertar(generic.CreateView):
     model = Partido
     context_object_name = 'Partido'
     template_name = 'form_Partido.html'
     form_class = Partidoform
     success_url=reverse_lazy("Partido:Partidos")
class Partidoeditar(generic.UpdateView):
     model = Partido
     context_object_name = 'Partido'
     template_name = 'form_Partido.html'
     form_class = Partidoform
     success_url=reverse_lazy("Partido:Partidos")
class Partidoeliminar(generic.DeleteView):
     model = Partido
     context_object_name = 'Partido'
     template_name = 'delete_Partido.html'
     form_class = Partidoform
     success_url=reverse_lazy("Partido:Partidos")
# Create your views here.
from django.shortcuts import render

# Create your views here.
