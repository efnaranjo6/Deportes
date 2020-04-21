
from django import forms
from PersonaNatural.models import PersonaNatural
class PersonaNaturalform(forms.ModelForm):
    class Meta:
        model = PersonaNatural
        fields = ['cedula','nombre']
        labels = {'cedula ': 'ingrese la  cedula',
                  'nombre': 'ingrese el nombre'
                 }
        widget={'cedula' : forms.TextInput(),
                'nombre' : forms.TextInput()
                 }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'})
