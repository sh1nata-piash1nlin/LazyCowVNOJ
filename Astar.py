# -*- coding: utf-8 -*-
"""
    @author: Nguyen "sh1nata" Duc Tri <22110082@student.hcmute.edu.vn>
"""
import math

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0 # root -> cur
        self.h = 0  #heuristic cur -> goal
        self.f = 0 #f(n)

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = [] # frontier queue
    closed_list = [] # explored set

    open_list.append(start_node)
    step_count = 0
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list): #f smaller is prefer
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node: #goal found
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []  #expansion domain
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] < 0 or node_position[0] > (len(maze)-1) or node_position[1] < 0 or node_position[1] > (len(maze[len(maze)-1])-1):
                continue
            if maze[node_position[0]][node_position[1]] != 0: #other is obs
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if any(child == closed_child for closed_child in closed_list):
                continue

            child.g = current_node.g + 1
            child.h = math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))
            child.f = child.g + child.h

            for open_node in open_list:  # child is already in frontier
                if child == open_node:
                    if child.g < open_node.g:
                        open_node.g = child.g
                        open_node.h = child.h
                        open_node.f = child.f
                        open_node.parent = current_node
                    break
            else:
                open_list.append(child)


if __name__ == '__main__':
    # maze =     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    goal = (0, 9)

    path = astar(maze, start, goal)
    print(path)

















