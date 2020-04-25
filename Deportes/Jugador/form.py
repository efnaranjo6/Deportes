from django import forms
from Jugador.models import Jugador
class Jugadorform(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre','fechanacimineto']
        labels = {'fechanacimineto ': 'ingrese la  fechanacimineto'
                 }
        widget={'nombre' : forms.TextInput(),
                 'fechanacimineto' : forms.TextInput(),
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if(field == 'fechanacimineto'):
                 self.fields[field].widget.attrs.update({'id':'datepicker'})
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
