import pygame
import os
import math

def get_animacion(path : str, columnas : int, filas : int, flip = False):
    lista = []
    surface_imagen = pygame.image.load(path)
    fotograma_ancho = int(surface_imagen.get_width()/columnas)
    fotograma_alto = int(surface_imagen.get_height()/filas)
    x = 0
    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            if flip == True:
                surface_fotograma = pygame.transform.flip(surface_fotograma, True, False)
            lista.append(surface_fotograma)
    return lista

