from django.db import models

class Ordenes(models.Model):
    id_orden = models.CharField(primary_key=True, max_length=6)
    id_cliente = models.IntegerField()
    fecha_orden = models.DateField(null=False, blank=False)
    total = models.FloatField()
    estado = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=100)
    comentarios = models.TextField()

    def __str__(self):
        return f"Orden {self.id_orden} - Cliente {self.id_cliente}"
