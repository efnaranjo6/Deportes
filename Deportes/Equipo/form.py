from django import forms
from Equipo.models import Equipo
class Equipoform(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre','ano_creacion','Empresa','PersonaNatural','Ciudad']
        labels = {'nombre ': 'ingrese el  nombre ',
                  'ano_creacion': 'ingrese el ano_creacion',
                  'Empresa ': 'ingrese la Empresa',
                  'Ciudad': 'ingrese el ciudad'
                  }
        widget={'nombre' : forms.TextInput(),
                'ano_creacion' : forms.TextInput(),
                'Empresa' : forms.TextInput(),
                'PersonaNatural' : forms.TextInput(),
                'Ciudad' : forms.TextInput()
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
