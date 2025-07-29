from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Serie, CalificacionSerie,CalificacionPelicula
from .forms import PeliculaForm, SerieForm, CalificacionPeliculaForm, CalificacionSerieForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def inicio(request):
    return render(request,'mi_primer_app/inicio.html')
# PELÍCULAS


def lista_peliculas(request):
    titulo = request.GET.get("titulo", "")
    peliculas = Pelicula.objects.filter(titulo__icontains=titulo) if titulo else Pelicula.objects.all()
    return render(request, "mi_primer_app/peliculas.html", {"peliculas": peliculas, "titulo": titulo})

def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    calificaciones = CalificacionPelicula.objects.filter(pelicula=pelicula)

    return render(request, 'mi_primer_app/detalle_pelicula.html', {
        'pelicula': pelicula,
        'calificaciones': calificaciones
    })


@login_required
def agregar_pelicula(request):
    if request.method == 'POST':
        form_pelicula = PeliculaForm(request.POST, request.FILES)
        form_calificacion = CalificacionPeliculaForm(request.POST)
        
        if form_pelicula.is_valid() and form_calificacion.is_valid():
            nueva_pelicula = form_pelicula.save()
            
            nueva_calificacion = form_calificacion.save(commit=False)
            nueva_calificacion.pelicula = nueva_pelicula
            nueva_calificacion.usuario = request.user  # si tienes usuario en el modelo calificación
            nueva_calificacion.save()
            
            return redirect('detalle_pelicula', pk=nueva_pelicula.pk)
    else:
        form_pelicula = PeliculaForm()
        form_calificacion = CalificacionPeliculaForm()
    
    return render(request, 'mi_primer_app/agregar_pelicula.html', {
        'form_pelicula': form_pelicula,
        'form_calificacion': form_calificacion,
    })


def calificar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = CalificacionPeliculaForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.pelicula = pelicula
            calificacion.save()
            return redirect('detalle_pelicula', pk=pk)
    else:
        form = CalificacionPeliculaForm()
    return render(request, 'peliculas/calificar.html', {'form': form, 'pelicula': pelicula})

def buscar_peliculas(request):
    titulo = request.GET.get('titulo', '')
    peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, 'mi_primer_app/peliculas.html', {'peliculas': peliculas, 'titulo': titulo})

# SERIES

def lista_series(request):
    titulo = request.GET.get("titulo", "")
    series = Serie.objects.filter(titulo__icontains=titulo) if titulo else Serie.objects.all()
    return render(request, 'mi_primer_app/series.html', {'series': series})

def detalle_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    calificaciones = CalificacionSerie.objects.filter(serie=serie)

    return render(request, 'mi_primer_app/detalle_serie.html', {
        'serie': serie,
        'calificaciones': calificaciones,
    })


@login_required
def agregar_serie(request):
    if request.method == 'POST':
        form_serie = SerieForm(request.POST, request.FILES)
        form_calificacion = CalificacionSerieForm(request.POST)

        if form_serie.is_valid() and form_calificacion.is_valid():
            nueva_serie = form_serie.save()

            nueva_calificacion = form_calificacion.save(commit=False)
            nueva_calificacion.serie = nueva_serie
            nueva_calificacion.usuario = request.user
            nueva_calificacion.save()

            return redirect('detalle_serie', pk=nueva_serie.pk)
    else:
        form_serie = SerieForm()
        form_calificacion = CalificacionSerieForm()

    return render(request, 'mi_primer_app/agregar_serie.html', {
        'form_serie': form_serie,
        'form_calificacion': form_calificacion,
    })

def calificar_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    if request.method == 'POST':
        form = CalificacionSerieForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.serie = serie
            calificacion.save()
            return redirect('detalle_serie', pk=pk)
    else:
        form = CalificacionSerieForm()
    return render(request, 'series/calificar.html', {'form': form, 'serie': serie})
