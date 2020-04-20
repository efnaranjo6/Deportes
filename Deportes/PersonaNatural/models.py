from django.db import models

# Create your models here.
# Create your models here.

class PersonaNatural(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.cedula=self.cedula
        self.nombre= self.nombre
        super(PersonaNatural,self).save()
class Meta:
      verbose_name_plural='Personas Naturales'
