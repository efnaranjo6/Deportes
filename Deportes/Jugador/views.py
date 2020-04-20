from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Jugador.models import Jugador
from Jugador.form import  Jugadorform

# vistas .

class Jugadorview(generic.ListView):
    model = Jugador
    template_name = 'listar_Jugador.html'
    context_object_name = 'Jugador'
class Jugadorinsertar(generic.CreateView):
     model = Jugador
     context_object_name = 'Jugador'
     template_name = 'form_Jugador.html'
     form_class = Jugadorform
     success_url=reverse_lazy("Jugador:Jugadors")
class Jugadoreditar(generic.UpdateView):
     model = Jugador
     context_object_name = 'Jugador'
     template_name = 'form_Jugador.html'
     form_class = Jugadorform
     success_url=reverse_lazy("Jugador:Jugadors")
class Jugadoreliminar(generic.DeleteView):
     model = Jugador
     context_object_name = 'Jugador'
     template_name = 'delete_Jugador.html'
     form_class = Jugadorform
     success_url=reverse_lazy("Jugador:Jugadors")
# Create your views here.
