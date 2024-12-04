from django.db import models

class Ordenes(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()
    puesto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"
