from django.urls import path,include
from JugadorDetalle.views import JugadorDetalleinsertar,JugadorDetalleeditar,JugadorDetalleeliminar,JugadorDetalleview

urlpatterns = [
path('', JugadorDetalleview.as_view(), name='JugadorDetalles'),
path('JugadorDetalle/new', JugadorDetalleinsertar.as_view(), name='Isertar'),
path('JugadorDetalle/Editar/<int:pk>', JugadorDetalleeditar.as_view(), name='Editar'),
path('JugadorDetalle/eliminar/<int:pk>', JugadorDetalleeliminar.as_view(), name='Eliminar'),

]
