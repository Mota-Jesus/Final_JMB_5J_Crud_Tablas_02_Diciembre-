from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    direccion = models.TextField()
    fecha_registro = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre}"
