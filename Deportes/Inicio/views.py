from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import  LoginRequiredMixin
class Inicio(LoginRequiredMixin,generic.TemplateView):
    template_name="home.html"
    login_url='Inicio:login'
