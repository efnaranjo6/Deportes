from django.db import models

from Equipo.models import Equipo
from JugadorTemporada.models import JugadorTemporada


# Create your models here.
class Alineacion(models.Model):

    min_ingreso = models.CharField(max_length=200)
    min_salida = models.CharField(max_length=200)
    Equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    JugadorTemporada=models.ForeignKey(JugadorTemporada, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):

        self.DetallePartido= self.DetallePartido
        super(DetalleEvento,self).save()
class Meta:
      verbose_name_plural='Partidos'
