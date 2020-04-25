from django import forms
from Equipo.models import Equipo
class Equipoform(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre','ano_creacion','Empresa','Ciudad']
        labels = {'nombre ': 'ingrese el  nombre ',
                  'ano_creacion': 'ingrese el ano_creacion',
                  'Empresa ': 'ingrese la Empresa',
                  'Ciudad': 'ingrese el ciudad'
                  }
        widget={'nombre' : forms.TextInput(),
                'ano_creacion' : forms.TextInput(),
                'Empresa' : forms.TextInput(),

                'Ciudad' : forms.TextInput()
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if(field == 'ano_creacion'):
                self.fields[field].widget.attrs.update({'id':'datepicker'})
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
