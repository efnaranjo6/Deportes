
from django import forms
from Partido.models import Partido
class Partidoform(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['fecha','hora','Descripccion','Estadio','Arbitro']
        labels = {'fecha ': 'ingrese la  fecha ',
                  'hora': 'ingrese la hora',
                  'Descripccion ': 'ingrese la  Descripccion',
                  'Estadio': 'ingrese la Estadio',
                  'Arbitro ': 'ingrese el  Arbitro',
                 }
        widget={'fecha' : forms.TextInput(),
                'hora' : forms.TextInput(),
                'Descripccion' : forms.TextInput(),
                'Estadio' : forms.TextInput(),
                'Arbitro' : forms.TextInput()
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if(field == 'fecha'):
                self.fields[field].widget.attrs.update({'id':'datepicker'})
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
