from django import forms
from Empresa.models import Empresa
class Empresaform(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre','representante','email','ciudad']
        labels = {'nombre ': 'ingrese el  nombre ',
                  'representante': 'ingrese el representante',
                  'email ': 'ingrese el email',
                  'ciudad': 'ingrese el ciudad',
                  }
        widget={'nombre' : forms.TextInput(),
                'representante' : forms.TextInput(),
                'email' : forms.TextInput(),
                'ciudad' : forms.TextInput(),
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
