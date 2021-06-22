from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id Categoría')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre Categoría')

    def __str__(self):
        return  self.nombreCategoria


class TipoAlimento(models.Model):
    idTipo = models.IntegerField(primary_key=True,verbose_name='Id Tipo Alimento')
    descripcion = models.CharField(max_length=50,verbose_name='Tipo Alimento')

    def __str__(self):
        return self.descripcion

class Alimento(models.Model):
    idAlimento = models.IntegerField(primary_key=True,verbose_name='Id Alimento')
    nombre = models.CharField(max_length=50,verbose_name='Alimento')
    descripcion = models.CharField(max_length=100,verbose_name='Descripcion Alimento')
    precio = models.IntegerField(verbose_name='Precio')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    tipoAlimento = models.ForeignKey(TipoAlimento,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class postulacionConcurso(models.Model):
    idPostulacion = models.AutoField(primary_key=True,verbose_name='Id Postulacion')
    nombreAlimento = models.CharField(max_length=50,verbose_name='Alimento')
    descripcionAlimento = models.CharField(max_length=100,verbose_name='Descripcion Alimento')
    precioAlimento = models.IntegerField(verbose_name='Precio')    

    def __str__(self):
        return self.nombreAlimento