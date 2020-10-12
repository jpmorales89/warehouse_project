from django.db import models

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)

def __str__(self):
    return self.nombre
