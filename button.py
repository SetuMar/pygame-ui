import pygame
import text as text_obj

class Button(text_obj.Text):
    def __init__(self, text, position, text_color, font_name, font_size, text_opacity=255, text_shadow=False, text_shadow_color= (255, 0, 0), text_shadow_padding= pygame.math.Vector2(2, 2), text_shadow_opacity = 255, button_color = (0, 0, 255), alt_button_color = (0, 255, 0), button_padding = pygame.math.Vector2(0, 0), custom_sprites = None, button_shadow = False, button_shadow_color= (255, 0, 0), button_shadow_padding= pygame.math.Vector2(2, 2), button_shadow_opacity = 255):
        text_obj.Text.__init__(self, text, position, text_color, font_name, font_size, text_opacity, text_shadow, text_shadow_color, text_shadow_padding, text_shadow_opacity)

        self.sprites = None
        self.button = None

        self.button_padding = button_padding

        if custom_sprites is None:
            self.button = pygame.Surface((font_size * len(text)/2 + self.button_padding.x, font_size + self.button_padding.y))

            self.button_color = button_color
            self.alt_button_color = alt_button_color
            self.button.fill(self.button_color)
        else:
            self.sprites = custom_sprites
            self.button = self.sprites[0]

        self.button_shadow_color = None
        self.button_shadow = None
        self.button_shadow_padding = None
        self.button_shadow_opacity = None

        if button_shadow is True:
            self.button_shadow_color = button_shadow_color
            self.button_shadow = pygame.Surface((self.button.get_width(), self.button.get_height()))
            self.button_shadow_padding = button_shadow_padding
            self.button_shadow_opacity = button_shadow_opacity

            self.button_shadow.set_alpha(self.button_shadow_opacity)

        self.button_rect = self.button.get_rect()
        self.button_rect.center = position
    
    def draw(self, display):

        if self.button_shadow_color != None:
            display.blit(self.button_shadow, self.button_rect.top + self.button_shadow_padding.x, self.button_rect.left + self.button_shadow_padding.y)

        display.blit(self.button, self.button_rect.topleft)

        if self.shadow_text != None:
            display.blit(self.shadow_text, self.rect.topleft + self.shadow_padding)

        display.blit(self.text, self.rect.topleft)
    
    def check_press(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            if self.sprites == None:
                self.button.fill(self.alt_button_color)
            else:
                self.button = self.sprites[1]
            
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
        else:
            if self.sprites == None:
                self.button.fill(self.button_color)
            else:
                self.button = self.sprites[0]

            return False