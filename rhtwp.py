# -*- coding: utf-8 -*-
"""
    @author: Nguyen "sh1nata" Duc Tri <22110082@student.hcmute.edu.vn>
    link to vid on Youtube:
    #My note: the given video above doesn't contain the GUI (or animation) part, I have just added it and forgot recording the video. Iam sorry if it doesn't give enough eviden

"""
from collections import deque
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


#mqh ACTION and cost action.
#no se tra ve voi depth nho nhat nma chua chac cost action nho nhat
#no se tra ve optimal sol neu path_cost f(d) la ham khong giam theo do sau.  f(1) <= f(2)
#do sau tang len, path cost tang len

# class Problem():
#     def __init__(self, initial, goal=None):
#         self.initial = initial
#         self.goal = goal
#
#     def actions(self, state): #state = 1, 2, 3, 4, 5 etc.
#         return ["Action1", "Action2"]
#
#
#     def result(self, state, action):
#         return state + action
#
#     def goal_test(self, state):
#         return state == self.goal
#
#     def path_cost(self, current_cost, state1, action, state2):
#         return current_cost+1
#
#     def value(self): #for optimization
#         pass


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

def BFS(problem):
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            if child.state not in explored and child.state not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

inf = 35
def iterative_deepening_search(problem):
    all_states = []
    for depth in range(0, inf):
        result, states_at_depth = depth_limited_search(problem, depth)
        all_states.extend(states_at_depth)
        if result != "cutoff":
            return result, all_states
    return None, all_states

def make_node(state):
    return Node(state)

def depth_limited_search(problem, limit=100):
    return recursive_dls(make_node(problem.initial), problem, limit)

def recursive_dls(node, problem, limit):
    #node = Node(problem.initial)
    all_states = [node.state]
    if problem.goal_test(node.state):
        return node, all_states
    elif limit == 0:
        return "cutoff", all_states #this indicates no sol within search lim
    else:
        flag = False #cutoff not occur
        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            result, child_states = recursive_dls(child, problem, limit - 1)
            all_states.extend(child_states)
            if result == "cutoff":
                flag = True
            elif result != None:
                return result, all_states
        return ("cutoff", all_states) if flag else (None, all_states)


#Visualization part

class PuzzleApp:
    def __init__(self, root, problem, solution, all_states):
        self.root = root
        self.root.title("Iterative Deepening Search Visualization")

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.problem = problem
        self.solution = solution

        self.board = np.array(self.problem.initial).reshape((3, 3))
        self.rectangles = {}
        self.texts = {}

        self.solution_states = self.get_solution_states()  # Get the states from the solution path
        self.draw_grid()
        self.animate_solution()

    def get_solution_states(self):
        """Generate a list of states corresponding to the solution path."""
        current_state = self.problem.initial
        states = [current_state]
        for action in self.solution:
            current_state = self.problem.result(current_state, action)
            states.append(current_state)
        return states

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(3):
            for j in range(3):
                x0, y0 = j * 100, i * 100
                x1, y1 = x0 + 100, y0 + 100
                self.rectangles[(i, j)] = self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")
                if self.board[i][j] != 0:
                    self.texts[(i, j)] = self.canvas.create_text((x0 + 50, y0 + 50), text=str(self.board[i][j]), font=("Helvetica", 24))

    def animate_solution(self):
        self.anim_idx = 0
        self.states = self.solution_states  # Now use the solution states for the animation
        self.root.after(500, self.update_board)

    def update_board(self):
        if self.anim_idx < len(self.states):
            self.board = np.array(self.states[self.anim_idx]).reshape((3, 3))
            self.draw_grid()
            self.anim_idx += 1
            self.root.after(500, self.update_board)



class EightPuzzleProblem:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    def __init__(self, initial, goal=(0,1,2,3,4,5,6,7,8)):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)
        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')
        return possible_actions

    def result(self, state, action):
        blank = self.find_blank_square(state)
        new_state = list(state)
        weight = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': +1}
        around = blank + weight[action]
        new_state[blank], new_state[around] = new_state[around], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, current_cost, state1, action, state2):
        return current_cost+1

    def find_blank_square(self, state):  #idx of blank square
        return state.index(0)


if __name__ == '__main__':
    root = tk.Tk()
    problem = EightPuzzleProblem(initial=(3, 1, 2, 6, 0, 8, 7, 5, 4), goal=(0, 1, 2, 3, 4, 5, 6, 7, 8))
    # result1 = BFS(problem)
    # print(result1.solution())
    result2, all_states = iterative_deepening_search(problem)
    print(result2.solution())

    app = PuzzleApp(root, problem, result2.solution() if result2 else None, all_states)
    root.mainloop()


