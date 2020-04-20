from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Ciudad.models import Ciudad
from Ciudad.form import  Ciudadform

# vistas .

class Ciudadview(generic.ListView):
    model = Ciudad
    template_name = 'listar_Ciudad.html'
    context_object_name = 'Ciudad'
class Ciudadinsertar(generic.CreateView):
     model = Ciudad
     context_object_name = 'Ciudad'
     template_name = 'form_Ciudad.html'
     form_class = Ciudadform
     success_url=reverse_lazy("Ciudad:Ciudads")
class Ciudadeditar(generic.UpdateView):
     model = Ciudad
     context_object_name = 'Ciudad'
     template_name = 'form_Ciudad.html'
     form_class = Ciudadform
     success_url=reverse_lazy("Ciudad:Ciudads")
class Ciudadeliminar(generic.DeleteView):
     model = Ciudad
     context_object_name = 'Ciudad'
     template_name = 'delete_Ciudad.html'
     form_class = Ciudadform
     success_url=reverse_lazy("Ciudad:Ciudads")
# Create your views here.
