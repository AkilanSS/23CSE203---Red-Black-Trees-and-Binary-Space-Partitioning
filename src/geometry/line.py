import pygame
from src.core.renderable import Renderable

class Line(Renderable):
    """A drawable line segment."""
    def __init__(self, start_pos, end_pos, color, width=2, layer=0):
        super().__init__(layer)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width

    def draw(self, surface, camera_offset=(0, 0)):
        """Draws the line to the surface with camera offset."""
        offset_x, offset_y = camera_offset
        # Adjust world coordinates to screen coordinates
        start_screen_pos = (self.start_pos[0] - offset_x, self.start_pos[1] - offset_y)
        end_screen_pos = (self.end_pos[0] - offset_x, self.end_pos[1] - offset_y)
        pygame.draw.line(surface, self.color, start_screen_pos, end_screen_pos, self.width)