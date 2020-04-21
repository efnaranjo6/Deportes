from django import forms
from Arbitro.models import Arbitro
class Arbitroform(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields = ['certificado','nombre']
        labels = {'certificado ': 'ingrese el  nombre del estadion',
                  'nombre': 'ingrese la capacidad de asistentes',

                 }
        widget={'certificado' : forms.TextInput(),
                'nombre' : forms.TextInput(),

                }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class':'form-control'})
