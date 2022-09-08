import pygame

class Transition:
    def __init__(self):
        self.objects = self.__dict__
    
    def lerp(self, new_position, duration):
        for obj in self.objects.values():
            if type(obj) is pygame.Rect:
                obj.center = pygame.math.Vector2.lerp(pygame.math.Vector2(obj.center), new_position, duration)
    
    def opacity_change(self, new_opacity, duration):
        def lerp(a, b, t):
            return a + (b - a) * t

        for obj in self.objects.values():
            if type(obj) is pygame.Surface:
                obj = obj.set_alpha(lerp(obj.get_alpha(), new_opacity, duration))
    
    def place(self, position):
        for obj in self.objects.values():
            if type(obj) is pygame.Rect:
                obj.center = position