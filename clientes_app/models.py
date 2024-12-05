from django.db import models

class Clientes(models.Model):
    id_clientes = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()
    fecha_reg = models.DateField(null=False, blank=False)
    codigo_postal = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"