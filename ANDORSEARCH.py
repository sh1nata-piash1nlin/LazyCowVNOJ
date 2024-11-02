# -*- coding: utf-8 -*-
"""
    @author: Nguyen "sh1nata" Duc Tri <22110082@student.hcmute.edu.vn>
    # Solve N-queens problems using AND-OR-SEARCH algorithm
"""
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        #next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
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

    def goal_test(self, state):
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))


def and_or_graph_search(problem):
    return or_search(problem.initial, problem, [])

def or_search(state, problem, path):
    if problem.goal_test(state):
        return []
    if state in path:
        return None
    for action in problem.actions(state):
        result_state = problem.result(state, action)  # Get the new state after action
        plan = and_search([result_state], problem, path + [state])
        if plan is not None:
            return [action, plan]

def and_search(states, problem, path):
    plan = {}
    for s in states:
        sub_plan = or_search(s, problem, path)
        if sub_plan is None:
            return None
        plan[s] = sub_plan
    return plan

if __name__ == '__main__':
    no_of_queens = 15
    problem1 = NQueensProblem(no_of_queens)

    result2 = and_or_graph_search(problem1)
    print(result2)