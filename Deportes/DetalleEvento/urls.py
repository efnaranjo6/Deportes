from django.urls import path,include
from DetalleEvento.views import DetalleEventoinsertar,DetalleEventoeditar,DetalleEventoeliminar,DetalleEventoview

urlpatterns = [
path('', DetalleEventoview.as_view(), name='DetalleEventos'),
path('DetalleEvento/new', DetalleEventoinsertar.as_view(), name='Isertar'),
path('DetalleEvento/Editar/<int:pk>', DetalleEventoeditar.as_view(), name='Editar'),
path('DetalleEvento/eliminar/<int:pk>', DetalleEventoeliminar.as_view(), name='Eliminar'),

]
