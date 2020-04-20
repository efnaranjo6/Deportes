from django.urls import path,include
from Equipo.views import Equipoinsertar,Equipoeditar,Equipoeliminar,Equipoview

urlpatterns = [
path('', Equipoview.as_view(), name='Equipos'),
path('Equipo/new', Equipoinsertar.as_view(), name='Isertar'),
path('Equipo/Editar/<int:pk>', Equipoeditar.as_view(), name='Editar'),
path('Equipo/eliminar/<int:pk>', Equipoeliminar.as_view(), name='Eliminar'),

]
