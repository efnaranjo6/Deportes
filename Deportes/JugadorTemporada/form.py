from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from JugadorTemporada.models import JugadorTemporada
from JugadorTemporada.form import  JugadorTemporadaform

# vistas .

class JugadorTemporadaview(generic.ListView):
    model = JugadorTemporada
    template_name = 'listar_JugadorTemporada.html'
    context_object_name = 'JugadorTemporada'
class JugadorTemporadainsertar(generic.CreateView):
     model = JugadorTemporada
     context_object_name = 'JugadorTemporada'
     template_name = 'form_JugadorTemporada.html'
     form_class = JugadorTemporadaform
     success_url=reverse_lazy("JugadorTemporada:JugadorTemporadas")
class JugadorTemporadaeditar(generic.UpdateView):
     model = JugadorTemporada
     context_object_name = 'JugadorTemporada'
     template_name = 'form_JugadorTemporada.html'
     form_class = JugadorTemporadaform
     success_url=reverse_lazy("JugadorTemporada:JugadorTemporadas")
class JugadorTemporadaeliminar(generic.DeleteView):
     model = JugadorTemporada
     context_object_name = 'JugadorTemporada'
     template_name = 'delete_JugadorTemporada.html'
     form_class = JugadorTemporadaform
     success_url=reverse_lazy("JugadorTemporada:JugadorTemporadas")
# Create your views here.
