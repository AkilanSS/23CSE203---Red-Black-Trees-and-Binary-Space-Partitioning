import pygame
from src.core.renderable import Renderable

class Circle(Renderable):
    def __init__(self, pos, color, radius, layer=0,):
        super().__init__(layer)
        self.pos = pos
        self.color = color
        self.radius = radius
    
    def draw(self, surface, camera_offset=(0,0)):
        offset_x, offset_y = camera_offset
        center = (self.pos[0] - offset_x, self.pos[1] - offset_y)
        pygame.draw.circle(surface, self.color, center, self.radius, width=0)
        