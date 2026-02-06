from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return self.titulo

    def clean(self):
        # Precio no negativo
        if self.precio < 0:
            raise ValidationError("El precio no puede ser negativo.")

        # Un usuario no puede tener dos productos con el mismo título
        repetido = Producto.objects.filter(
            vendedor=self.vendedor,
            titulo=self.titulo
        )
        if self.pk:
            repetido = repetido.exclude(pk=self.pk)

        if repetido.exists():
            raise ValidationError("Ya tienes un producto con ese título.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
