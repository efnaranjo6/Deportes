from django import forms
from Estadio.models import Estadio
class Estadioform(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['nombre','capacidad','ano_construccion']
        labels = {'nombre ' : 'ingrese el  nombre del estadion',
                  'capacidad': 'ingrese la capacidad de asistentes',
                  'ano_construccion':'ingres el año de construccion'
                 }
        widget={'nombre' : forms.TextInput(),
                'capacidad' : forms.TextInput(),
                'ano_construccion' : forms.TextInput()
                }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if(field == 'ano_construccion'):
                print("perro")
                self.fields[field].widget.attrs.update({'id':'datepicker'})
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
