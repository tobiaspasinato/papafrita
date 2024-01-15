import pygame
from functions import *
from constants import *

class pared:
    def __init__(self, left : int, top : int, width : int, height : int) -> None:
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect((self.left, self.top), (self.width, self.height))
    
    def crear_muro(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
    
    def crear_collision(self, item):
        pass