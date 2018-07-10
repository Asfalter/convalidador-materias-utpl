from django.db import models

class Titulacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    titulacion = models.ForeignKey(Titulacion, on_delete=models.CASCADE)

    CICLO_CHOICES = (
        ('PRIMERO','PRIMERO'),
        ('SEGUNDO','SEGUNDO'),
        ('TERCERO','TERCERO'),
        ('CUARTO','CUARTO'),
        ('QUINTO','QUINTO'),
        ('SEXTO','SEXTO'),
        ('SEPTIMO','SEPTIMO'),
        ('OCTAVO','OCTAVO'),
        ('NOVENO','NOVENO'),
        ('DECIMO','DECIMO'),
    )

    ciclo = models.CharField(max_length=20, choices=CICLO_CHOICES, default='PRIMERO')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


