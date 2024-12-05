from django.db import models

class Inventario(models.Model):
    id_inventario = models.CharField(primary_key=True, max_length=6)
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField(null=False, blank=False)
    fecha_vencimiento = models.DateField(null=False, blank=False)
    id_proveedor = models.IntegerField()
    Notas = models.TextField()

    def __str__(self):
        return f"Inventario {self.id_inventario} - Producto {self.id_producto}"
