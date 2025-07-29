from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('pelicula/agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('pelicula/<int:pk>/calificar/', views.calificar_pelicula, name='calificar_pelicula'),
    path('pelicula/buscar/', views.buscar_peliculas, name='buscar-peliculas'),

    path('series/', views.lista_series, name='lista_series'),
    path('serie/<int:pk>/', views.detalle_serie, name='detalle_serie'),
    path('serie/agregar/', views.agregar_serie, name='agregar_serie'),
    path('serie/<int:pk>/calificar/', views.calificar_serie, name='calificar_serie'),
    path('series/', views.lista_series, name='lista_series')
]
