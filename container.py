import pygame

class Container():
    def __init__(self, position):
        self.objects = self.__dict__
        self.position = position
    
    def lerp_container(self, lerp_position, time):
        old_pos = self.position
        change_amt = pygame.math.Vector2.lerp(self.position, lerp_position, time) - old_pos

        self.position += change_amt

        for obj in self.objects.values():
            try:
                obj.place(obj.rect.center + change_amt)
            except:
                pass
    
    def draw_container(self, display):
        for obj in self.objects.values():
            try:
                obj.draw(display)
            except:
                pass