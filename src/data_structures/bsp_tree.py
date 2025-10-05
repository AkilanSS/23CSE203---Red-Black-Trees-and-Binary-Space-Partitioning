from src.geometry.utils import classify_line, classify_point, split_line
from src.geometry.line import Line

class Node:
    def __init__(self, line : Line):
        self.div = line
        self.front = None
        self.back = None
        self.onLines : list[Line]

class BSP:
    def __init__(self, linesInScreen : list[Line]):
        self.root = None
        self.lines = linesInScreen

    def build(self, lines : list[Line]) -> Node:
        if not lines:
            return None

        (dividing_line, line_idx) = self.find_optimal_divide_line(lines)

        currNode = Node(dividing_line)
        front_list = []
        back_list = []

        if len(lines) == 1:
            return currNode

        lines.remove(dividing_line)
        for line in lines:
            orientation = classify_line(dividing_line, line)
            if orientation == 1:
                front_list.append(dividing_line)
            elif orientation == -1:
                back_list.append(dividing_line)
            elif orientation == 2:
                front_split, back_split = split_line(line, dividing_line)
                if front_split is not None:
                    front_list.append(front_split)
                if front_split is not None:
                    back_list.append(back_split)
            else:
                currNode.onLines.add(line)

        currNode.front = self.build(front_list)
        currNode.back = self.build(back_list)

        return currNode

    def traverse(self, node, camera_pos, result):

        view = classify_point(camera_pos, node.div)
        if view == 1:
            self.traverse(node.back, camera_pos, result)
            result.extend(node.lines)
            self.traverse(node.front, camera_pos, result)
        elif view == -1 :
            self.traverse(node.front, camera_pos, result)
            result.extend(node.lines)
            self.traverse(node.back, camera_pos, result)
        else:
            self.traverse(node.front, camera_pos, result)
            self.traverse(node.back, camera_pos, result)

    def find_optimal_divide_line(self, lines : list[Line]) -> tuple[Line, int]:
        return (lines[0], 0)