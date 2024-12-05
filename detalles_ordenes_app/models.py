from django.db import models

class Detalles(models.Model):
    id_detalles = models.CharField(primary_key=True, max_length=6)
    id_orden = models.IntegerField()
    id_empleado = models.IntegerField()
    direccion_envio = models.TextField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Orden {self.id_orden} - Producto {self.id_producto}"
