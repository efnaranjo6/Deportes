from django import forms
from Evento.models import Evento
class Eventoform(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre']
        labels = {'nombre ': 'ingrese el  nombre'
                 }
        widget={'nombre' : forms.TextInput(),

                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
