from django.urls import path,include
from Alineacion.views import Alineacioninsertar,Alineacioneditar,Alineacioneliminar,Alineacionview

urlpatterns = [
path('', Alineacionview.as_view(), name='Alineaciones'),
path('Alineacion/new', Alineacioninsertar.as_view(), name='Isertar'),
path('Alineacion/Editar/<int:pk>', Alineacioneditar.as_view(), name='Editar'),
path('Alineacion/eliminar/<int:pk>', Alineacioneliminar.as_view(), name='Eliminar'),

]
