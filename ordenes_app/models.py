from django.db import models

class Ordenes(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField()
    id_empleado = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_orden = models.DateField(null=False, blank=False)
    total = models.FloatField()

    def __str__(self):
        return f"Orden {self.id_orden} - Cliente {self.id_cliente}"
