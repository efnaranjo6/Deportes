from django.urls import path,include
from Ciudad.views import Ciudadinsertar,Ciudadeditar,Ciudadeliminar,Ciudadview

urlpatterns = [
path('', Ciudadview.as_view(), name='Ciudades'),
path('Ciudad/new', Ciudadinsertar.as_view(), name='Isertar'),
path('Ciudad/Editar/<int:pk>', Ciudadeditar.as_view(), name='Editar'),
path('Ciudad/eliminar/<int:pk>', Ciudadeliminar.as_view(), name='Eliminar'),

]
