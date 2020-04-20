from django.urls import path,include
from DetallePartido.views import DetallePartidoinsertar,DetallePartidoeditar,DetallePartidoeliminar,DetallePartidoview

urlpatterns = [
path('', DetallePartidoview.as_view(), name='DetallePartidos'),
path('DetallePartido/new', DetallePartidoinsertar.as_view(), name='Isertar'),
path('DetallePartido/Editar/<int:pk>', DetallePartidoeditar.as_view(), name='Editar'),
path('DetallePartido/eliminar/<int:pk>', DetallePartidoeliminar.as_view(), name='Eliminar'),

]
