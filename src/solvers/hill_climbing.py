from .base import Solver, Result
from ..engine import *
import math
import random
import time

class HillClimbing(Solver):
    def __init__(self, objective):
        super().__init__(objective)

class SteepestAscent(HillClimbing):
    def __init__(self, objective, max_iterations=10000):
        super().__init__(objective)
        self.max_iterations = max_iterations

    def solve(self, initial_state):
        current_state = initial_state
        current_objective = self.objective(current_state)
        
        t = 0
        objective_history = [self.objective(current_state)]

        start_time = time.perf_counter()

        for t in range(1, self.max_iterations + 1):
            successor = get_all_neighbors(current_state) # awake all successors of the current state
            successor_value = [self.objective(successor[i]) for i in range(len(successor))] # returns all successors values
            neighbor_state = successor[successor_value.index(max(successor_value))] # returns successor with the highest value as neighbor
            neighbor_objective = self.objective(neighbor_state) # returns neighbor value
            
            if neighbor_objective > current_objective:
                current_state = neighbor_state
                current_objective = neighbor_objective
            else:
                break
            
            objective_history.append(self.objective(current_state))

        end_time = time.perf_counter()
        runtime = end_time - start_time

        return Result(
            initial_state, 
            current_state, 
            objective_history, 
            t, 
            runtime
        )

class SidewaysMove(HillClimbing):
    def __init__(self, objective, max_sideways_moves=10, max_iterations=10000):
        super().__init__(objective)
        self.max_sideways_moves = max_sideways_moves
        self.max_iterations = max_iterations

    def solve(self, initial_state):
        current_state = initial_state
        current_objective = self.objective(current_state)

        t = 0
        sideways_move = 0
        objective_history = [self.objective(current_state)]

        start_time = time.perf_counter()

        for t in range(1, self.max_iterations + 1):
            successor = get_all_neighbors(current_state) # awake all successors of the current state
            successor_value = [self.objective(successor[i]) for i in range(len(successor))] # returns all successors values
            neighbor_state = successor[successor_value.index(max(successor_value))] # returns successor with the highest value as neighbor
            neighbor_objective = self.objective(neighbor_state) # returns neighbor value
            
            if neighbor_objective > current_objective:
                current_state = neighbor_state
                current_objective = neighbor_objective
                sideways_move = 0 # reset sideways_move counter if neighbor_state > current_state
            elif neighbor_objective == current_objective and sideways_move < self.max_sideways_moves:
                current_state = neighbor_state
                current_objective = neighbor_objective
                sideways_move += 1
            else:
                break
            
            objective_history.append(self.objective(current_state))

        end_time = time.perf_counter()
        runtime = end_time - start_time

        return Result(
            initial_state, 
            current_state, 
            objective_history, 
            t, 
            runtime,
            sideways_moves=sideways_move
        )
