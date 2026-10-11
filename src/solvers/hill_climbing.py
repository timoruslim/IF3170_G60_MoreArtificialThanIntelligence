from .base import Solver, Result
from ..engine import *
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

class Stochastic(HillClimbing):
    def __init__(self, objective, max_random_successor_iterations=10, max_iterations=10000):
        super().__init__(objective)
        self.max_random_successor_iterations = max_random_successor_iterations
        self.max_iterations = max_iterations

    def solve(self, initial_state):
        current_state = initial_state
        current_objective = self.objective(current_state)

        t = 0
        random_successor_iterations = 0
        objective_history = [self.objective(current_state)]
        random_successor_per_value = []

        start_time = time.perf_counter()

        for t in range(1, self.max_iterations + 1):
            neighbor_state = get_random_neighbor(current_state) # awake a random successor of the current state
            neighbor_objective = self.objective(neighbor_state) # returns the successor value
            if neighbor_objective > current_objective:
                current_state = neighbor_state
                current_objective = neighbor_objective
                random_successor_per_value.append(random_successor_iterations)
                random_successor_iterations = 0 # reset random_successor_iterations counter if neighbor_state > current_state
            else:
                random_successor_iterations += 1
            
            if random_successor_iterations >= self.max_random_successor_iterations:
                random_successor_per_value.append(random_successor_iterations)
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
            random_successor_iterations=random_successor_per_value
        )

class RandomRestart(HillClimbing):
    def __init__(self, objective, max_restarts=15, max_iterations_per_restart=100):
        super().__init__(objective)
        self.max_restarts = max_restarts
        self.max_iterations_per_restart = max_iterations_per_restart

    def solve(self, initial_state):
        starts = []
        best_state = []
        best_objective = []

        restarts = 0
        iteration_per_restart = []
        objective_history = [[-float('inf') for iteration in range(1, self.max_iterations_per_restart + 1)] for restart in range(1, self.max_restarts + 1)]

        start_time = time.perf_counter()

        for restart in range(1, self.max_restarts + 1):
            initial_state = State.initialize_placements("random") # initialize random starting state
            starts.append(initial_state)
            for iteration in range(1, self.max_iterations_per_restart + 1):
                current_state = initial_state
                current_objective = self.objective(current_state)
                
                successor = get_all_neighbors(current_state) # awake all successors of the current state
                successor_value = [self.objective(successor[i]) for i in range(len(successor))] # returns all successors values
                neighbor_state = successor[successor_value.index(max(successor_value))] # returns successor with the highest value as neighbor
                neighbor_objective = self.objective(neighbor_state) # returns neighbor value
            
                if neighbor_objective > current_objective:
                    current_state = neighbor_state
                    current_objective = neighbor_objective
                else:
                    break

                objective_history[restart-1][iteration-1] = self.objective(current_state)

            best_state.append(current_state)
            best_objective.append(self.objective(current_state))
            restarts += 1
            iteration_per_restart.append(iteration)

        final_state = best_state[best_objective.index(max(best_objective))] # returns the best state from all restarts
        final_objective = self.objective(final_state)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        
        return Result(
            starts, 
            final_state, 
            best_objective, 
            iteration_per_restart, 
            runtime,
            total_restarts = restarts,
            final_objective_value = final_objective
        )