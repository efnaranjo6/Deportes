from django.db import models

# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length=200)
    fechanacimineto = models.DateField()
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre=self.nombre
        self.fechanacimineto= self.fechanacimineto
        super(Jugador,self).save()
class Meta:
      verbose_name_plural='Jugadores'
