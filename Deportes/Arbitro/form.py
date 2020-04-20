from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Arbitro.models import Arbitro
from Arbitro.form import  Arbitroform

# vistas .

class Arbitroview(generic.ListView):
    model = Arbitro
    template_name = 'listar_Arbitro.html'
    context_object_name = 'Arbitro'
class Arbitroinsertar(generic.CreateView):
     model = Arbitro
     context_object_name = 'Arbitro'
     template_name = 'form_Arbitro.html'
     form_class = Arbitroform
     success_url=reverse_lazy("Arbitro:Arbitros")
class Arbitroeditar(generic.UpdateView):
     model = Arbitro
     context_object_name = 'Arbitro'
     template_name = 'form_Arbitro.html'
     form_class = Arbitroform
     success_url=reverse_lazy("Arbitro:Arbitros")
class Arbitroeliminar(generic.DeleteView):
     model = Arbitro
     context_object_name = 'Arbitro'
     template_name = 'delete_Arbitro.html'
     form_class = Arbitroform
     success_url=reverse_lazy("Arbitro:Arbitros")
# Create your views here.
