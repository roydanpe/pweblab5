from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Libro(models.Model):  # Modelo para los libros
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    resumen = models.TextField()

    def __str__(self):
        return self.titulo


class Reseña(models.Model):  # Modelo para las reseñas
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reseñas')  # Relación con Libro
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario de Django
    calificacion = models.PositiveSmallIntegerField()  # Por ejemplo, del 1 al 5
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.usuario.username} sobre "{self.libro.titulo}"'
