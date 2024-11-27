from django.contrib import admin

# Register your models here.
from .models import Libro, Reseña

admin.site.register(Libro)
admin.site.register(Reseña)
