from django.urls import path,include
from Evento.views import Eventoinsertar,Eventoeditar,Eventoeliminar,Eventoview

urlpatterns = [
path('', Eventoview.as_view(), name='Eventos'),
path('Evento/new', Eventoinsertar.as_view(), name='Isertar'),
path('Evento/Editar/<int:pk>', Eventoeditar.as_view(), name='Editar'),
path('Evento/eliminar/<int:pk>', Eventoeliminar.as_view(), name='Eliminar'),

]
