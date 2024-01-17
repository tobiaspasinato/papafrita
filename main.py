import pygame
from functions import *
from constants import *
from clases.player import player
from pygame.locals import *

milis = pygame.time.Clock()
#holis
pygame.init() #Se inicializa pygame
screen = pygame.display.set_mode([1150, 750]) #Se crea una ventana
pygame.display.set_caption("Cuphead trucho") # Nombre de la pestaña
imagen_level1 = pygame.image.load("papafrita/img/fondo.jpeg") # Cargar imagen del fondo
level1_img = pygame.transform.scale(imagen_level1, (LARGO_PANTALLA, ANCHO_PANTALLA))
running = True
direccion = False

player1 = player(500,500)

while running:
    accion_personaje = "stay"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# Se verifica si el usuario cerro la ventana
            running = False
    pressed_keys = pygame.key.get_pressed()
    if True in pressed_keys:
        if pressed_keys[K_a]:
            player1.control(-10, 0)
            accion_personaje = "walk"
            direccion = False
        if pressed_keys[K_d]:
            player1.control(10, 0)
            accion_personaje = "walk"
            direccion = True
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    screen.blit(level1_img,(0,0)) # Ubicacion del fondo
    player1.upgrade()
    player1.dibujar(screen, accion_personaje, direccion)
    pygame.display.flip()# Muestra los cambios en la pantalla
    milis.tick(FPS)
pygame.quit() # Fin