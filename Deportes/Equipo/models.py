from django.db import models
from Ciudad.models import Ciudad
from Empresa.models import Empresa
from PersonaNatural.models import PersonaNatural
# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    ano_creacion = models.DateField()
    Empresa=models.OneToOneField(Empresa, on_delete=models.CASCADE)
    PersonaNatural=models.ForeignKey(PersonaNatural, on_delete=models.CASCADE)
    Ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre=self.nombre
        self.ano_creacion= self.ano_creacion
        self.Empresa= self.Empresa
        self.PersonaNatural= self.PersonaNatural
        self.Ciudad= self.Ciudad
        super(Equipo,self).save()
class Meta:
      verbose_name_plural='Equipo'
