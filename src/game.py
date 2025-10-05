# src/game.py
import pygame
import sys
from .config import *
from .core.renderer import Renderer
from .geometry.line import Line
from .geometry.camera import Camera
from  .data_structures.bsp_tree import BSP, Node

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Modular Draw Lines Example")
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.renderer = Renderer()
        
        self.drawing = False
        self.start_pos = None

    def run(self):
        while self.is_running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    self.drawing = True
                    mx, my = pygame.mouse.get_pos()
                    self.start_pos = (mx + self.renderer.camera_offset[0], my + self.renderer.camera_offset[1])
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.drawing:
                    self.drawing = False
                    mx, my = pygame.mouse.get_pos()
                    end_pos = (mx + self.renderer.camera_offset[0], my + self.renderer.camera_offset[1])
                    new_line = Line(self.start_pos, end_pos, BLACK, width=2)
                    self.renderer.add(new_line)
                    self.start_pos = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.drawing = False
                    mx, my = pygame.mouse.get_pos()
                    camera = Camera((mx + self.renderer.camera_offset[0], my + self.renderer.camera_offset[1]), GREEN, 5)
                    self.renderer.add(camera)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    renderTree = BSP(self.renderer.lineObjects)
                    rootBSP : Node  = renderTree.build(self.renderer.lineObjects)
                    renderTree.traverse(rootBSP, self.renderer.cameraPos, result= None)


    def _update(self):
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
        self.screen.fill(WHITE)
        
        self.renderer.draw(self.screen)
        
        if self.drawing and self.start_pos:
            mx, my = pygame.mouse.get_pos()
            start_screen_pos = (self.start_pos[0] - self.renderer.camera_offset[0], 
                                self.start_pos[1] - self.renderer.camera_offset[1])
            pygame.draw.line(self.screen, RED, start_screen_pos, (mx, my), 2)
            
        pygame.display.flip()