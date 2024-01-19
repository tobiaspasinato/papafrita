import pygame
from functions import *

class player:
    def __init__(self, x : int, y : int) -> None:
        self.stay_r = get_animacion_player("papafrita/img/PC Computer - Cuphead Dont Deal With the Devil - Cuphead/Idle/cuphead_idle_", 4)
        self.stay_l = get_animacion_player("papafrita/img/PC Computer - Cuphead Dont Deal With the Devil - Cuphead/Idle/cuphead_idle_", 4, True)
        self.run_r = get_animacion_player("papafrita/img/PC Computer - Cuphead Dont Deal With the Devil - Cuphead/Run/Normal/cuphead_run_", 15)
        self.run_l = get_animacion_player("papafrita/img/PC Computer - Cuphead Dont Deal With the Devil - Cuphead/Run/Normal/cuphead_run_", 15, True)
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
    
    def jump(self):
        self.move_y = self.move_y - 100
    
    def gravedad(self):
        self.move_y = self.move_y + 10
    
    def upgrade(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.move_x = 0
        self.move_y = 0
    
    def dibujar(self, screen, accion, direccion):
        if direccion == True:
            if accion == "stay":
                self.frame = 0
                self.animation = self.stay_r
                self.image = self.animation[self.frame]
            elif accion == "walk":
                self.animation = self.run_r
                self.image = self.animation[self.frame]
        else:
            if accion == "stay":
                self.frame = 0
                self.animation = self.stay_l
                self.image = self.animation[self.frame]
            elif accion == "walk":
                self.animation = self.run_l
                self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)