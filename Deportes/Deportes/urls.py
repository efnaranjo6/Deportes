"""Deportes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(('Inicio.urls','Inicio'),namespace='Inicio')),
    path('Estadios/',include(('Estadio.urls','Estadio'),namespace='Estadio')),
     path('Alineacion/',include(('Alineacion.urls','Alineacion'),namespace='Alineacion')),
    path('Arbitro/',include(('Arbitro.urls','Arbitro'),namespace='Arbitro')),
    path('Ciudad/',include(('Ciudad.urls','Ciudad'),namespace='Ciudad')),
    path('DetallesE/',include(('DetalleEvento.urls','DetalleEvento'),namespace='DetalleE')),
    path('DetallesP/',include(('DetallePartido.urls','DetallePartido'),namespace='DetalleP')),
    path('Equipo/',include(('Equipo.urls','Equipo'),namespace='Equipo')),
    path('Estadio/',include(('Estadio.urls','Estadio'),namespace='Estadio')),
    path('Empresa/',include(('Empresa.urls','Empresa'),namespace='Empresa')),
    path('Evento/',include(('Evento.urls','Evento'),namespace='Evento')),
    path('Jugador/',include(('Jugador.urls','Jugador'),namespace='Jugador')),
    path('JugadorT/',include(('JugadorTemporada.urls','JugadorTemporada'),namespace='JugadorT')),
    path('Partido/',include(('Partido.urls','Partido'),namespace='Partido')),
    path('PersonaN/',include(('PersonaNatural.urls','PersonaN'),namespace='PersonaN')),

]
