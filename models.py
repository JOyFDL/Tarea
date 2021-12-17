from django.db import models

# Create your models here.
class Libreria(models.Model):

    id = models.AutoField(primary_key=True)
    libro = models.CharField(max_length=60)
    escritor = models.CharField(max_length=100)
    fecha = models.DateField()
    tapa = models.ImageField(
        upload_to = 'tapa/%Y/%m/%d',
        blank = True,
        verbose_name = ('Tapa del Libro')
    )

class Meta:
    verbose_name = ('Libreria')
    verbose_name_plural = ('Librerias')

def __str__(self):
    return self.libro