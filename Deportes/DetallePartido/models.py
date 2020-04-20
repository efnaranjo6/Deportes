from django.db import models

from Equipo.models import Equipo
from Partido.models import Partido

# Create your models here.
class DetallePartido(models.Model):

    Equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Partido=models.ForeignKey(Partido, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.equipo=self.equipo
        self.partido= self.partido
        super(DetallePartido,self).save()
class Meta:
      verbose_name_plural='Partidos'
