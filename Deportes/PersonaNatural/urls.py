from django.urls import path,include
from PersonaNatural.views import PersonaNaturalinsertar,PersonaNaturaleditar,PersonaNaturaleliminar,PersonaNaturalview

urlpatterns = [
path('', PersonaNaturalview.as_view(), name='PersonaNaturales'),
path('PesonaNatural/new', PersonaNaturalinsertar.as_view(), name='Isertar'),
path('PesonaNatural/Editar/<int:pk>', PersonaNaturaleditar.as_view(), name='Editar'),
path('PesonaNatural/eliminar/<int:pk>', PersonaNaturaleliminar.as_view(), name='Eliminar'),

]
