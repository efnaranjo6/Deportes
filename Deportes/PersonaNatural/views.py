from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views import generic
from django.http import  HttpResponse
from django.shortcuts import render
from PersonaNatural.models import PersonaNatural
from PersonaNatural.form import  PersonaNaturalform

# vistas .

class PersonaNaturalview(generic.ListView):
    model = PersonaNatural
    template_name = 'listar_PersonaNatural.html'
    context_object_name = 'PersonaNatural'
class PersonaNaturalinsertar(generic.CreateView):
     model = PersonaNatural
     context_object_name = 'PersonaNatural'
     template_name = 'form_PersonaNatural.html'
     form_class = PersonaNaturalform
     success_url=reverse_lazy("PersonaN:PersonaNaturales")
class PersonaNaturaleditar(generic.UpdateView):
     model = PersonaNatural
     context_object_name = 'PersonaNatural'
     template_name = 'form_PersonaNatural.html'
     form_class = PersonaNaturalform
     success_url=reverse_lazy("PersonaN:PersonaNaturales")
class PersonaNaturaleliminar(generic.DeleteView):
     model = PersonaNatural
     context_object_name = 'PersonaNatural'
     template_name = 'delete_PersonaNatural.html'
     form_class = PersonaNaturalform
     success_url=reverse_lazy("PersonaN:PersonaNaturales")
# Create your views here.
