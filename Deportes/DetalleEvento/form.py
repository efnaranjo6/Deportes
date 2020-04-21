from django import forms
from DetalleEvento.models import DetalleEvento

class DetalleEventoform(forms.ModelForm):
    class Meta:
        model = DetalleEvento
        fields = ['Evento','Alineacion','DetallePartido','Descripccion']
        labels = {'Evento ': 'ingrese el  nombre del estadion',
                  'Alineacion': 'ingrese la capacidad de asistentes',
                  'DetallePartido ': 'ingrese el  nombre del estadio',
                  'Descripccion ': 'ingrese el  nombre del estadio'
                 }
        widget={'Evento' : forms.TextInput(),
                'Alineacion' : forms.TextInput(),
                'DetallePartido' : forms.TextInput(),
                'Descripccion' : forms.TextInput()
                }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
