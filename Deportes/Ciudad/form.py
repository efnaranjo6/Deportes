from django import forms
from Ciudad.models import Ciudad
class Ciudadform(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre','poblacion']
        labels = {'Evento ': 'ingrese el  nombre del evento',
                  'poblacion': 'ingrese la capacidad de poblacion'

                 }
        widget={'nombre' : forms.TextInput(),
                'poblacion' : forms.TextInput(),

                }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
