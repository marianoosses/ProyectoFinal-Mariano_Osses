from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    temporadas = models.PositiveIntegerField()
    fecha_estreno = models.DateField()
    imagen = models.ImageField(upload_to='series/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class CalificacionPelicula(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='calificaciones')
    puntaje = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True, null=True)

class CalificacionSerie(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='calificaciones')
    puntaje = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True, null=True)
    

