import pygame

from src.geometry.utils import classify_line, classify_point, split_line
from src.geometry.line import Line
from src.config import *
from src.core.renderer import Renderer

class Node:
    def __init__(self, line : Line):
        self.div = line
        self.front = None
        self.back = None
        self.onLines = []

class BSP:
    def __init__(self, linesInScreen : list[Line], renderScene):
        self.root = None
        self.lines = linesInScreen
        self.renderScene : Renderer = renderScene
        self.original_colors = {}  

    def build(self, lines : list[Line]) -> Node:
        if not lines:
            return None

        lines_copy = lines.copy()
        (dividing_line, line_idx) = self.find_optimal_divide_line(lines_copy)
        if dividing_line not in self.original_colors:
            self.original_colors[dividing_line] = dividing_line.color

        currNode = Node(dividing_line)
        front_list = []
        back_list = []

        if len(lines_copy) == 1:
            return currNode

        lines_copy.remove(dividing_line)
        
        for line in lines_copy:
            orientation = classify_line(dividing_line, line)
            
            if orientation == 1:  
                front_list.append(line)  
            elif orientation == -1:  
                back_list.append(line)  
            elif orientation == 2:  
                front_split, back_split = split_line(dividing_line, line)
                
                self.renderScene.objects.remove(line)
                self.renderScene.lineObjects.remove(line)
                
                if front_split:
                    self.renderScene.lineObjects.append(front_split)
                    self.renderScene.objects.append(front_split)
                    front_list.append(front_split)
                    self.original_colors[front_split] = front_split.color
                    
                if back_split:  
                    self.renderScene.lineObjects.append(back_split)
                    self.renderScene.objects.append(back_split)
                    back_list.append(back_split)
                    self.original_colors[back_split] = back_split.color
            else: 
                currNode.onLines.append(line)

        currNode.front = self.build(front_list)
        currNode.back = self.build(back_list)

        return currNode

    def traverse(self, node : Node, camera_pos, result, screen):
        if node is None:
            return
        
        view = classify_point(camera_pos, node.div)
        
        if view == 1: 
            self.traverse(node.back, camera_pos, result, screen)
            result.append(node.div)
            self._visualize_line(node.div, screen)
            self.traverse(node.front, camera_pos, result, screen)
        elif view == -1: 
            self.traverse(node.front, camera_pos, result, screen)
            result.append(node.div)
            self._visualize_line(node.div, screen)
            self.traverse(node.back, camera_pos, result, screen)
        else: 
            self.traverse(node.front, camera_pos, result, screen)
            self.traverse(node.back, camera_pos, result, screen)

    def _visualize_line(self, line, screen):
        line.color = RED
        screen.fill(WHITE)
        self.renderScene.draw(screen)
        pygame.display.flip()
        pygame.time.delay(500)
        if line in self.original_colors:
            line.color = self.original_colors[line]

    def find_optimal_divide_line(self, lines : list[Line]) -> tuple[Line, int]:
        return (lines[0], 0)