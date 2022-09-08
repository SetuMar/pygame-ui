import pygame
import transitions

class Text(transitions.Transition):
    def __init__(self, text, position, color, font_name, font_size, opacity=255, shadow=False, shadow_color= (255, 0, 0), shadow_padding= pygame.math.Vector2(2, 2), shadow_opacity = 255):
        transitions.Transition.__init__(self)
        
        self.font_size = font_size
        self.font = pygame.font.Font(font_name, self.font_size)

        self.font_color = color
        self.text = self.font.render(text, True, self.font_color)
        self.text.set_alpha(opacity)

        self.shadow_text = None
        self.shadow_padding = None
        self.shadow_color = None
        self.shadow_opacity = None

        if shadow is True:
            self.shadow_color = shadow_color
            self.shadow_text = self.font.render(text, True, self.shadow_color)
            self.shadow_padding = shadow_padding
            self.shadow_opacity = shadow_opacity
            self.shadow_text.set_alpha(self.shadow_opacity)

        self.save_position = position

        self.rect = self.text.get_rect()
        self.rect.center = self.save_position
    
    def draw(self, display):
        if self.shadow_text != None:
            display.blit(self.shadow_text, self.rect.topleft + self.shadow_padding)

        display.blit(self.text, self.rect.topleft)
    
    def update_text(self, new_text):
        old_text = self.text
        self.text = self.font.render(new_text, True, self.font_color)
        self.text.set_alpha(old_text.get_alpha())

        if self.shadow_text is not None:
            self.shadow_text = self.font.render(new_text, True, self.shadow_color)

        self.rect = self.text.get_rect()
        self.rect.center = self.save_position