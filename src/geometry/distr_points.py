import pygame
import random
from src.geometry.circle import Circle
from src.config import *
from src.core.renderer import Renderer


class DistibutePoints:
    def __init__(self, screen, number):
        self.circles = []
        self.radius = 1
        self.screen  : Renderer = screen
        self.number = number
        
    def generate(self):
        for _ in range(self.number):
            x = random.randint(self.radius, WIDTH - self.radius)
            y = random.randint(self.radius, HEIGHT - self.radius)
            self.circles.append(Circle((x, y) , BLUE, self.radius))
    
    def render(self):
        for circle in self.circles:
            self.screen.objects.append(circle)
