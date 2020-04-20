
from django.db import models

from Estadio.models import Estadio
from Arbitro.models import Arbitro

# Create your models here.
class Partido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    Descripccion = models.CharField(max_length=200)
    Estadio=models.ForeignKey(Estadio, on_delete=models.CASCADE)
    Arbitro=models.ForeignKey(Arbitro, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.fecha=self.fecha
        self.hora= self.hora
        self.Descripccion= self.Descripccion
        self.Estadio= self.Estadio
        self.Arbitro= self.Arbitro
        super(Partido,self).save()
class Meta:
      verbose_name_plural='Partidos'
