from django.db import models
from Participante.models import MiInformacion
 

# Modelo Garaje

class Modelo(models.Model):
    año = models.PositiveIntegerField()

    def __str__(self):
        return str(self.año)

class Caracteristicas(models.Model):
    descripcion = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion

class Automovil(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    motor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    caracteristicas = models.ManyToManyField(Caracteristicas)

    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    cliente = models.ForeignKey(MiInformacion, on_delete=models.CASCADE)
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)
    fecha_compra = models.DateField()

    def __str__(self):
        return f"{self.cliente} - {self.automovil}"