from django.urls import path,include
from Estadio.views import Estadioinsertar,Estadioeditar,Estadioeliminar,Estadioview

urlpatterns = [
path('', Estadioview.as_view(), name='Estadios'),
path('Estadio/new', Estadioinsertar.as_view(), name='Isertar'),
path('Estadio/Editar/<int:pk>', Estadioeditar.as_view(), name='Editar'),
path('Estadio/eliminar/<int:pk>', Estadioeliminar.as_view(), name='Eliminar'),

]
