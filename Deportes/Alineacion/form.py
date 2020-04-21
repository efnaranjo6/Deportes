from django import forms
from Alineacion.models import Alineacion
class Alineacionform(forms.ModelForm):
    class Meta:
        model = Alineacion
        fields = ['min_ingreso','min_salida','Equipo','JugadorTemporada']
        labels = {'minuto de ingreso ' : 'ingrese el  nombre del estadion',
                  'minuto de salida': 'ingrese la capacidad de asistentes',
                  'Equipo':'ingres el año de construccion',
                  'JugadorTemporada':'ingrese el Jugador Temporada',
                 }
        widget={'min_ingreso' : forms.TextInput(),
                'min_salida' : forms.TextInput(),
                'ano_construccion' : forms.TextInput(),
                'Equipo' : forms.TextInput(),
                'JugadorTemporada' : forms.TextInput(),
                }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
    
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
