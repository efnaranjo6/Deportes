from django.urls import path,include
from Arbitro.views import Arbitroinsertar,Arbitroeditar,Arbitroeliminar,Arbitroview

urlpatterns = [
path('', Arbitroview.as_view(), name='Arbitros'),
path('Arbitro/new', Arbitroinsertar.as_view(), name='Isertar'),
path('Arbitro/Editar/<int:pk>', Arbitroeditar.as_view(), name='Editar'),
path('Arbitro/eliminar/<int:pk>', Arbitroeliminar.as_view(), name='Eliminar'),

]
