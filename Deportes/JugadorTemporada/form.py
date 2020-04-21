
from django import forms
from JugadorTemporada.models import JugadorTemporada
class JugadorTemporadaform(forms.ModelForm):
    class Meta:
        model = JugadorTemporada
        fields = ['fechainicial','fechafinal','Equipo','Jugador']
        labels = {'fechainicial ': 'ingrese la  fecha inicial',
                  'fechafinal ': 'ingrese la  fecha final',
                  'Equipo ': 'ingrese la  Equipo',
                  'Jugador ': 'ingrese la  Jugador',
                 }
        widget={'fechainicial' : forms.TextInput(),
                'fechafinal' : forms.TextInput(),
                'Equipo' : forms.TextInput(),
                'Jugador' : forms.TextInput(),
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
