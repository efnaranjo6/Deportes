from django import forms
from DetallePartido.models import DetallePartido
class DetallePartidoform(forms.ModelForm):
    class Meta:
        model = DetallePartido
        fields = ['Equipo','Partido']
        labels = {'Equipo ': 'ingrese el  nombre del estadion',
                  'Partido': 'ingrese el Partido',
                  }
        widget={'Equipo' : forms.TextInput(),
                'Partido' : forms.TextInput()
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
