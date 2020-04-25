from django import forms
from Arbitro.models import Arbitro
class Arbitroform(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields = ['certificado','nombreA']
        labels = {'certificado ': 'ingrese el  certificado',
                  'nombreA': 'ingrese El nombre',

                 }
        widget={'certificado' : forms.TextInput(),
                'nombrea' : forms.TextInput(),
                }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):

            self.fields[field].widget.attrs.update({
                'class':'form-control'})
