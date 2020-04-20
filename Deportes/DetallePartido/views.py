from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from DetallePartido.models import DetallePartido
from DetallePartido.form import  DetallePartidoform

# vistas .

class DetallePartidoview(generic.ListView):
    model = DetallePartido
    template_name = 'listar_DetallePartido.html'
    context_object_name = 'DetallePartido'
class DetallePartidoinsertar(generic.CreateView):
     model = DetallePartido
     context_object_name = 'DetallePartido'
     template_name = 'form_DetallePartido.html'
     form_class = DetallePartidoform
     success_url=reverse_lazy("DetallePartido:DetallePartidos")
class DetallePartidoeditar(generic.UpdateView):
     model = DetallePartido
     context_object_name = 'DetallePartido'
     template_name = 'form_DetallePartido.html'
     form_class = DetallePartidoform
     success_url=reverse_lazy("DetallePartido:DetallePartidos")
class DetallePartidoeliminar(generic.DeleteView):
     model = DetallePartido
     context_object_name = 'DetallePartido'
     template_name = 'delete_DetallePartido.html'
     form_class = DetallePartidoform
     success_url=reverse_lazy("DetallePartido:DetallePartidos")
# Create your views here.
