from django.contrib import admin

# Register your models here.
from .models import Pelicula, Serie, CalificacionPelicula, CalificacionSerie

register_models = [Pelicula, Serie, CalificacionPelicula,CalificacionSerie]

admin.site.register(register_models)
