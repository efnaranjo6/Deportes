from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from Empresa.models import Empresa
from Empresa.form import  Empresaform

# vistas .

class Empresaview(generic.ListView):
    model = Empresa
    template_name = 'listar_Empresa.html'
    context_object_name = 'Empresa'
class Empresainsertar(generic.CreateView):
     model = Empresa
     context_object_name = 'Empresa'
     template_name = 'form_Empresa.html'
     form_class = Empresaform
     success_url=reverse_lazy("Empresa:Empresas")
class Empresaeditar(generic.UpdateView):
     model = Empresa
     context_object_name = 'Empresa'
     template_name = 'form_Empresa.html'
     form_class = Empresaform
     success_url=reverse_lazy("Empresa:Empresas")
class Empresaeliminar(generic.DeleteView):
     model = Empresa
     context_object_name = 'Empresa'
     template_name = 'delete_Empresa.html'
     form_class = Empresaform
     success_url=reverse_lazy("Empresa:Empresas")
# Create your views here.
