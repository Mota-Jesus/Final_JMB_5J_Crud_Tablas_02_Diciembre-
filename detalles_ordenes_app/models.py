from django.db import models

class Detalles(models.Model):
    id_detalles = models.CharField(primary_key=True, max_length=6)
    id_orden = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()
    descuento = models.FloatField()

    def __str__(self):
        return f"Orden {self.id_orden} - Producto {self.id_producto}"
