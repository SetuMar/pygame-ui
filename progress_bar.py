import pygame
import transitions

class ProgressBar(transitions.Transition):
    def __init__(self, position, size, color, align="left"):
        transitions.Transition.__init__(self)
        
        self.image = pygame.Surface(size)
        self.color = color
        self.image.fill(self.color)
        self.image.set_alpha(255)

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.max_progress = size.x
        self.lerp_amt = 1

        self.align = align

    def update(self, fill_decimal, lerp_time):
        copy_rect = self.rect.copy()

        old_image = self.image
        self.rect.size = pygame.math.Vector2.lerp(pygame.math.Vector2(self.rect.size), pygame.math.Vector2(self.max_progress * fill_decimal, self.rect.height), lerp_time)
        lerped_dimensions = pygame.math.Vector2.lerp(pygame.math.Vector2(old_image.get_width(), old_image.get_height()), pygame.math.Vector2(self.max_progress * fill_decimal, old_image.get_height()), lerp_time)
        
        self.image = pygame.Surface(lerped_dimensions)
        self.image.fill(self.color)
        self.image.set_alpha(old_image.get_alpha())

        match self.align:
            case "left":
                self.rect.topleft = copy_rect.topleft
            case "right":
                self.rect.topright = copy_rect.topright
            case "center":
                self.rect.center = copy_rect.center

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)