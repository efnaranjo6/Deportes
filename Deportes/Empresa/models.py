from django.db import models
from Ciudad.models import Ciudad

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    representante = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.nombre=self.nombre
        self.representante= self.representante
        self.email= self.email
        self.ciudad= self.ciudad
        super(Empresa,self).save()
class Meta:
      verbose_name_plural='Empresas'
