# -*- coding: utf-8 -*-


import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, color, radius, move_x, move_y, bullet_speed=10):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.bullet_speed = bullet_speed
        self.move_x = move_x
        self.move_y = move_y
        
        self.rect = pygame.Rect(x, y, 0.000001, 0.000001)
    
        
    def draw(self, display_surface):
        
        self.x = self.x - self.move_x * self.bullet_speed
        self.y = self.y - self.move_y * self.bullet_speed
        
        self.rect = \
        pygame.draw.circle(display_surface, 
                           self.color, 
                           (self.x, self.y), 
                           self.radius, 0)