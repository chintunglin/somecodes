# -*- coding: utf-8 -*-

import pygame

class image_temp(pygame.sprite.Sprite):
    
    def __init__(self, path=None, center=(0, 0), image=None):
        
        pygame.sprite.Sprite.__init__(self)
        
        if image == None:
            self.image = pygame.image.load(path)
        
        else:
            self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def get_image_rect(self):
        
        return (self.image, self.rect)
    
    def reset_rect(self, center):
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def reset_object(self):
        pass
    