from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Evento.models import Evento
from Evento.form import  Eventoform

# vistas .

class Eventoview(generic.ListView):
    model = Evento
    template_name = 'listar_Evento.html'
    context_object_name = 'Evento'
class Eventoinsertar(generic.CreateView):
     model = Evento
     context_object_name = 'Evento'
     template_name = 'form_Evento.html'
     form_class = Eventoform
     success_url=reverse_lazy("Evento:Eventos")
class Eventoeditar(generic.UpdateView):
     model = Evento
     context_object_name = 'Evento'
     template_name = 'form_Evento.html'
     form_class = Eventoform
     success_url=reverse_lazy("Evento:Eventos")
class Eventoeliminar(generic.DeleteView):
     model = Evento
     context_object_name = 'Evento'
     template_name = 'delete_Evento.html'
     form_class = Eventoform
     success_url=reverse_lazy("Evento:Eventos")
# Create your views here.
