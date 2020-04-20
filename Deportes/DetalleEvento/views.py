from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from DetalleEvento.models import DetalleEvento
from DetalleEvento.form import  DetalleEventoform

# vistas .

class DetalleEventoview(generic.ListView):
    model = DetalleEvento
    template_name = 'listar_DetalleEvento.html'
    context_object_name = 'DetalleEvento'
class DetalleEventoinsertar(generic.CreateView):
     model = DetalleEvento
     context_object_name = 'DetalleEvento'
     template_name = 'form_DetalleEvento.html'
     form_class = DetalleEventoform
     success_url=reverse_lazy("DetalleEvento:DetalleEventos")
class DetalleEventoeditar(generic.UpdateView):
     model = DetalleEvento
     context_object_name = 'DetalleEvento'
     template_name = 'form_DetalleEvento.html'
     form_class = DetalleEventoform
     success_url=reverse_lazy("DetalleEvento:DetalleEventos")
class DetalleEventoeliminar(generic.DeleteView):
     model = DetalleEvento
     context_object_name = 'DetalleEvento'
     template_name = 'delete_DetalleEvento.html'
     form_class = DetalleEventoform
     success_url=reverse_lazy("DetalleEvento:DetalleEventos")
# Create your views here.
