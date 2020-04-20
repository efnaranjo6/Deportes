from django.db import models


# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    poblacion = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre=self.nombre
        self.poblacion= self.poblacion

        super(Ciudad,self).save()
class Meta:
      verbose_name_plural='Ciudades'
