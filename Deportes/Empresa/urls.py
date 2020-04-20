from django.urls import path,include
from Empresa.views import Empresainsertar,Empresaeditar,Empresaeliminar,Empresaview

urlpatterns = [
path('', Empresaview.as_view(), name='Empresas'),
path('Empresa/new', Empresainsertar.as_view(), name='Isertar'),
path('Empresa/Editar/<int:pk>', Empresaeditar.as_view(), name='Editar'),
path('Empresa/eliminar/<int:pk>', Empresaeliminar.as_view(), name='Eliminar'),

]
