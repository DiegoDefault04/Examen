from django.db import models

#Modelo Minformacion
class MiInformacion(models.Model):
    SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO)

    def __str__(self):
        return self.nombre