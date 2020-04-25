from django.db import models

# Create your models here.
class Arbitro(models.Model):
    certificado = models.CharField(max_length=200)
    nombreA = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.nombreA)
    def save(self):
        self.certificado=self.certificado
        self.nombreA= self.nombreA
        super(Arbitro,self).save()
class Meta:
      verbose_name_plural='Arbitros'
