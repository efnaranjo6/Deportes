from django.db import models

# Create your models here.
class Arbitro(models.Model):
    certificado = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        self.certificado=self.certificado
        self.nombre= self.nombre
        super(Arbitro,self).save()
class Meta:
      verbose_name_plural='Arbitros'
