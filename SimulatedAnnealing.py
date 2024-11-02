# -*- coding: utf-8 -*-
"""
    @author: Nguyen "sh1nata" Duc Tri <22110082@student.hcmute.edu.vn>
    # Solve N-queens problems using Simulated annealing algorithm
"""

import math
import numpy as np
import random


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
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node

class NQueensProblem:
    """
    Result: <Node (0, 4, 7, 5, 2, 6, 1, 3)>
    """
    def __init__(self, N):
        self.initial = tuple([0] + [-1] * (N - 1))  # -1: no queen in that column
        #index in tuple: col
        #value of idx : row  state presentation
        self.N = N

    def actions(self, state):
        if state[-1] != -1:  #last col has been filled by a queen or not ?
            return []
        else:
            col = state.index(-1) #return the index of the first occurrence of -1 in the state tuple, leftmost
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        col = state.index(-1)
        new = list(state[:]) # Make copy of current state = list
        new[col] = row # Place the nx queen in the given row in leftmost column.
        return tuple(new)

    def conflicted(self, state, row, col):
        #state[c] = earlier row
        return any(self.conflict(row, col, state[c], c) for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def value(self, node):
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return -num_conflicts



def schedule(t, k=20, lam=0.003, limit=1000):
    return (k * np.exp(-lam * t) if t < limit else 0)
# def schedule(t, k=20, c=1, limit=1000):
#     return (k / (1 + c * math.log(1 + t)) if t < limit else 0)

def simulated_annealing(problem):
    current = Node(problem.initial)
    inf = 1000
    for t in range(inf):   # time step
        Temperature = schedule(t)
        if Temperature == 0:
            return current.state
        next_nodes = current.expand(problem)
        if not next_nodes:
            return current.state
        next = random.choice(next_nodes)
        delta_E = problem.value(next) - problem.value(current)
        if delta_E > 0 or random.random() < math.exp(delta_E / Temperature):
            current = next



if __name__ == '__main__':
    no_of_queens = 8
    problem1 = NQueensProblem(no_of_queens)

    result1 = simulated_annealing(problem1)
    print(result1)

