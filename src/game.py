# src/game.py
import pygame
import sys
from .config import *
from .core.renderer import Renderer
from .geometry.line import Line

class Game:
    """Manages the main game loop, state, and events."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Modular Draw Lines Example")
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.renderer = Renderer()
        
        # Game state
        self.drawing = False
        self.start_pos = None

    def run(self):
        """The main game loop."""
        while self.is_running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

    def _handle_events(self):
        """Handles user input and other events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.drawing = True
                    mx, my = pygame.mouse.get_pos()
                    # Convert screen coordinates to world coordinates
                    self.start_pos = (mx + self.renderer.camera_offset[0], my + self.renderer.camera_offset[1])
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.drawing:
                    self.drawing = False
                    mx, my = pygame.mouse.get_pos()
                    # Convert screen coordinates to world coordinates
                    end_pos = (mx + self.renderer.camera_offset[0], my + self.renderer.camera_offset[1])
                    new_line = Line(self.start_pos, end_pos, BLACK, width=2)
                    self.renderer.add(new_line)
                    self.start_pos = None

    def _update(self):
        """Updates game state, like camera movement."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.renderer.camera_offset[0] -= CAMERA_SPEED
        if keys[pygame.K_RIGHT]:
            self.renderer.camera_offset[0] += CAMERA_SPEED
        if keys[pygame.K_UP]:
            self.renderer.camera_offset[1] -= CAMERA_SPEED
        if keys[pygame.K_DOWN]:
            self.renderer.camera_offset[1] += CAMERA_SPEED

    def _draw(self):
        """Renders everything to the screen."""
        self.screen.fill(WHITE)
        
        # Draw all permanent lines
        self.renderer.draw(self.screen)
        
        # Draw the temporary preview line while drawing
        if self.drawing and self.start_pos:
            mx, my = pygame.mouse.get_pos()
            # Start position is in world coords, mouse pos is in screen coords.
            # Convert start_pos to screen coords for drawing.
            start_screen_pos = (self.start_pos[0] - self.renderer.camera_offset[0], 
                                self.start_pos[1] - self.renderer.camera_offset[1])
            pygame.draw.line(self.screen, RED, start_screen_pos, (mx, my), 2)
            
        pygame.display.flip()