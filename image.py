import pygame

import transitions

class Image(transitions.Transition):
    def __init__(self, loaded_image, position):
        transitions.Transition.__init__(self)
        self.image = loaded_image
        self.image.set_alpha(255)
        
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)
    
    def update_opacity(self, new_opacity):
        self.image.set_alpha(new_opacity)
    
    def update_image(self, new_loaded_image):
        old_image = self.image
        self.image = new_loaded_image

        self.image.set_alpha(old_image.get_alpha())