from django.db import models

class Productos(models.Model):
    id_productos = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=100)
    fecha_añadido = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.nombre
