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
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Modular Draw Lines Example")
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.renderer = Renderer()
        
        self.drawing = False
        self.start_pos = None

        self.camera = None
        self.rootBSP = None
        self.renderTree = None

        self.fontBold = pygame.font.Font("src/assets/PixelifySans-Bold.ttf", 30)
        self.fontMedium = pygame.font.Font("src/assets/PixelifySans-Medium.ttf", 20)
        self.fontRegular = pygame.font.Font("src/assets/Jersey15-Regular.ttf", 30)
        self.fontSemiBold = pygame.font.Font("src/assets/PixelifySans-SemiBold.ttf", 30)

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
                    mx, my = pygame.mouse.get_pos()
                    self.renderer.cameraPos = (mx + self.renderer.camera_offset[0], my + self.renderer.camera_offset[1])
                    self.camera = Camera(self.renderer.cameraPos, GREEN, 5)
                    self.renderer.add(self.camera)
                if event.key == pygame.K_b:
                    linesToBuild = self.renderer.lineObjects.copy()
                    self.renderTree = BSP(linesToBuild, self.renderer)
                    self.rootBSP : Node  = self.renderTree.build(linesToBuild)
                
                if event.key == pygame.K_t:
                    traversal_order = []
                    self.renderTree.traverse(self.rootBSP, self.renderer.cameraPos, traversal_order, self.screen)
                    print(self.rootBSP)
                
                if event.key == pygame.K_r:
                    print("resetting camera")
                    self.renderer.remove(self.camera)


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

        titleText = self.fontBold.render("Optimal Object Lookup using RB trees and BSP trees", False, BLACK)
        instructionText1 = self.fontRegular.render("Drag your mouse to draw lines on the screen", False, BLACK)
        instructionText2 = self.fontRegular.render("Press C to place a camera under the cursor", False, BLACK)
        instructionText3 = self.fontRegular.render("Press B to build the BSP tree", False, BLACK)
        instructionText4 = self.fontRegular.render("Press T to traverse the tree", False, BLACK)
        instructionText5 = self.fontRegular.render("Press R to clear the camera position", False, BLACK)

        self.screen.blit(titleText, (10,10))
        self.screen.blit(instructionText1, (10, 680))
        self.screen.blit(instructionText2, (10, 700))
        self.screen.blit(instructionText3, (10, 720))
        self.screen.blit(instructionText4, (10, 740))
        self.screen.blit(instructionText5, (10, 760))
        
        if self.drawing and self.start_pos:
            mx, my = pygame.mouse.get_pos()
            start_screen_pos = (self.start_pos[0] - self.renderer.camera_offset[0], 
                                self.start_pos[1] - self.renderer.camera_offset[1])
            pygame.draw.line(self.screen, RED, start_screen_pos, (mx, my), 2)
            
        pygame.display.flip()