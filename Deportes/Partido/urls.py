from django.urls import path,include
from Partido.views import Partidoinsertar,Partidoeditar,Partidoeliminar,Partidoview

urlpatterns = [
path('', Partidoview.as_view(), name='Partidos'),
path('Partido/new', Partidoinsertar.as_view(), name='Isertar'),
path('Partido/Editar/<int:pk>', Partidoeditar.as_view(), name='Editar'),
path('Partido/eliminar/<int:pk>', Partidoeliminar.as_view(), name='Eliminar'),

]
