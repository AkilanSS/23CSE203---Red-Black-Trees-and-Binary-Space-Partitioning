import pygame
import sys

class Renderable:
    """Base class for anything that can be rendered."""
    def __init__(self, layer=0):
        self.layer = layer

    def draw(self, surface, camera_offset=(0, 0)):
        pass

class Line(Renderable):
    def __init__(self, start_pos, end_pos, color, width=2, layer=0):
        super().__init__(layer)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width

    def draw(self, surface, camera_offset=(0, 0)):
        offset_x, offset_y = camera_offset
        start = (self.start_pos[0] - offset_x, self.start_pos[1] - offset_y)
        end = (self.end_pos[0] - offset_x, self.end_pos[1] - offset_y)
        pygame.draw.line(surface, self.color, start, end, self.width)

class Renderer:
    """Manages and renders all objects."""
    def __init__(self):
        self.objects = []
        self.camera_offset = [0, 0]

    def add(self, obj):
        self.objects.append(obj)

    def draw(self, surface):
        for obj in sorted(self.objects, key=lambda o: o.layer):
            obj.draw(surface, self.camera_offset)

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Lines Example")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

renderer = Renderer()

drawing = False
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                drawing = True
                mx, my = pygame.mouse.get_pos()
                start_pos = (mx + renderer.camera_offset[0], my + renderer.camera_offset[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                mx, my = pygame.mouse.get_pos()
                end_pos = (mx + renderer.camera_offset[0], my + renderer.camera_offset[1])
                renderer.add(Line(start_pos, end_pos, BLACK, width=2, layer=0))
                start_pos = None

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        renderer.camera_offset[0] -= 5
    if keys[pygame.K_RIGHT]:
        renderer.camera_offset[0] += 5
    if keys[pygame.K_UP]:
        renderer.camera_offset[1] -= 5
    if keys[pygame.K_DOWN]:
        renderer.camera_offset[1] += 5

    screen.fill(WHITE)
    renderer.draw(screen)

    if drawing and start_pos:
        mx, my = pygame.mouse.get_pos()
        preview_end = (mx + renderer.camera_offset[0], my + renderer.camera_offset[1])
        pygame.draw.line(screen, RED, 
                         (start_pos[0] - renderer.camera_offset[0], start_pos[1] - renderer.camera_offset[1]),
                         (preview_end[0] - renderer.camera_offset[0], preview_end[1] - renderer.camera_offset[1]), 2)

    pygame.display.flip()
    clock.tick(60)