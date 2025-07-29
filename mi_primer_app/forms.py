from django import forms
from .models import Pelicula, Serie, CalificacionPelicula, CalificacionSerie

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'fecha_estreno', 'imagen']
        widgets = {
            'fecha_estreno': forms.DateInput(attrs={'type': 'date'}),
        }

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo', 'descripcion', 'temporadas', 'fecha_estreno', 'imagen']
        widgets = {
            'fecha_estreno': forms.DateInput(attrs={'type': 'date'}),
        }

class CalificacionPeliculaForm(forms.ModelForm):
    class Meta:
        model = CalificacionPelicula
        fields = ['puntaje', 'comentario']

class CalificacionSerieForm(forms.ModelForm):
    class Meta:
        model = CalificacionSerie
        fields = ['puntaje', 'comentario']
