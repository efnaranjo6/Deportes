from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        super(Evento,self).save()
class Meta:
      verbose_name_plural='Eventos'
