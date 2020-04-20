from django.urls import path,include
from PesonaNatural.views import PesonaNaturalinsertar,PesonaNaturaleditar,PesonaNaturaleliminar,PesonaNaturalview

urlpatterns = [
path('', PesonaNaturalview.as_view(), name='PesonaNaturales'),
path('PesonaNatural/new', PesonaNaturalinsertar.as_view(), name='Isertar'),
path('PesonaNatural/Editar/<int:pk>', PesonaNaturaleditar.as_view(), name='Editar'),
path('PesonaNatural/eliminar/<int:pk>', PesonaNaturaleliminar.as_view(), name='Eliminar'),

]
