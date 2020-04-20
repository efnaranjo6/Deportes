from django.urls import path,include
from JugadorTemporada.views import JugadorTemporadainsertar,JugadorTemporadaeditar,JugadorTemporadaeliminar,JugadorTemporadaview

urlpatterns = [
path('', JugadorTemporadaview.as_view(), name='JugadorTemporadas'),
path('JugadorTemporada/new', JugadorTemporadainsertar.as_view(), name='Isertar'),
path('JugadorTemporada/Editar/<int:pk>', JugadorTemporadaeditar.as_view(), name='Editar'),
path('JugadorTemporada/eliminar/<int:pk>', JugadorTemporadaeliminar.as_view(), name='Eliminar'),

]
