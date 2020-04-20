from django.db import models
from Equipo.models import Equipo
from Jugador.models import Jugador

# Create your models here.
class JugadorTemporada(models.Model):
    fechainicial = models.DateField()
    fechafinal = models.DateField()
    Equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Jugador=models.ForeignKey(Jugador, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.fechainicial=self.fechainicial
        self.fechafinal= self.fechafinal
        self.Equipo= self.Equipo
        self.Jugador= self.Jugador
        super(JugadorTemporada,self).save()
class Meta:
      verbose_name_plural='Jugadores'
