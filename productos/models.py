from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    CATEGORIAS = [
        ("tecnologia", "Tecnología"),
        ("hogar", "Hogar"),
        ("moda", "Moda"),
        ("deporte", "Deporte"),
        ("vehiculos", "Vehículos"),
        ("otros", "Otros"),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo
        
    