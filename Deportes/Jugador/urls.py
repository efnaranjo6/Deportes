from django.urls import path,include
from Jugador.views import Jugadorinsertar,Jugadoreditar,Jugadoreliminar,Jugadorview

urlpatterns = [
path('', Jugadorview.as_view(), name='Jugadors'),
path('Jugador/new', Jugadorinsertar.as_view(), name='Isertar'),
path('Jugador/Editar/<int:pk>', Jugadoreditar.as_view(), name='Editar'),
path('Jugador/eliminar/<int:pk>', Jugadoreliminar.as_view(), name='Eliminar'),

]
