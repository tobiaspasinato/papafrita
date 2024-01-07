import pygame
from functions import get_animacion

class player:
    def __init__(self, x : int, y : int) -> None:
        self.stay_r = get_animacion()
        self.stay_l = get_animacion()
        self.walk_r = get_animacion()
        self.walk_l = get_animacion()
        self.move_x = x
        self.move_y = y
        self.frame = 0
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        pass
    
    def control(self, x, y):
        self.move_x = x
        self.move_y = y
    
    def upgrade(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.move_x = 0
        self.move_y = 0