from django.db import models

from Evento.models import Evento
from DetallePartido.models import DetallePartido
from Alineacion.models import Alineacion

# Create your models here.
class DetalleEvento(models.Model):
     Evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
     Alineacion=models.ForeignKey(Alineacion, on_delete=models.CASCADE)
     DetallePartido=models.ForeignKey(DetallePartido, on_delete=models.CASCADE)
     Descripccion = models.CharField(max_length=200)
     def __str__(self):
        return '{}'.format(self.Alineacion)
     def save(self):
        self.Evento= self.Evento
        self.Alineacion= self.Alineacion
        self.DetallePartido= self.DetallePartido
        self.Descripccion= self.Descripccion
        super(DetalleEvento,self).save()
class Meta:
      verbose_name_plural='Eventos'
