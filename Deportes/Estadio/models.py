from django.db import models


# Create your models here.

class Estadio(models.Model):
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    ano_construccion = models.DateField()
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre=self.nombre
        self.capacidad= self.capacidad
        self.ano_construccion=self.ano_construccion
        super(Estadio,self).save()
class Meta:
      verbose_name_plural='Estadios'
